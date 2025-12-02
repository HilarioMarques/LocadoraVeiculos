from config import app, db
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuario, Veiculo, Locacao
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy import or_

from functools import wraps

# --------------------------
# DECORATORS DE AUTENTICAÇÃO
# --------------------------

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect("/login")
        return func(*args, **kwargs)
    return wrapper


def role_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # *** CORREÇÃO ESSENCIAL: AGORA VERIFICA A CHAVE 'usuario_role' ***
            if "usuario_role" not in session: 
                return redirect("/login")

            if session["usuario_role"] not in roles:
                return "Acesso negado", 403

            return func(*args, **kwargs)
        return wrapper
    return decorator

# --------------------------
# CONFIGURAÇÃO E ROTAS GERAIS
# --------------------------

app.secret_key = "SUA_CHAVE_SECRETA_AQUI"   # coloque qualquer string grande

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Sessão encerrada com sucesso!", "info")
    return redirect(url_for("landing"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha_hash, senha):
            session["usuario_id"] = usuario.id
            # *** CORREÇÃO: MANTEM A CHAVE 'usuario_role' PARA SER CONSISTENTE COM BASE.HTML E DECORATOR ***
            session["usuario_role"] = usuario.role 

            if usuario.role == "admin":
                return redirect("/admin/usuarios")
            elif usuario.role == "funcionario":
                return redirect("/funcionario")
            else:
                return redirect("/cliente")
        else:
            flash("Email ou senha inválidos.", "danger")
            
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        if Usuario.query.filter_by(email=email).first():
            flash("Este email já está cadastrado.", "danger")
            return redirect("/register")

        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.set_senha(senha)
        novo_usuario.role = "cliente" # Usuários se registram como clientes

        db.session.add(novo_usuario)
        db.session.commit()
        flash("Cadastro realizado com sucesso! Faça login para continuar.", "success")
        return redirect("/login")
        
    return render_template("register.html")

# --------------------------
# ROTAS DO ADMIN (USUÁRIOS)
# --------------------------

@app.route("/admin/usuarios")
@login_required
@role_required("admin") # CORRIGIDO
def admin_usuarios_list():
    usuarios = Usuario.query.all()
    return render_template("admin/usuarios_list.html", usuarios=usuarios)

@app.route("/admin/usuarios/novo", methods=["GET", "POST"])
@login_required
@role_required("admin") # CORRIGIDO
def admin_usuarios_novo():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form.get("senha")
        role = request.form["role"]

        if Usuario.query.filter_by(email=email).first():
            flash("Email já cadastrado.", "danger")
            return render_template("admin/usuarios_form.html", titulo="Novo Usuário")

        novo_usuario = Usuario(nome=nome, email=email, role=role)
        if senha:
            novo_usuario.set_senha(senha)
        
        db.session.add(novo_usuario)
        db.session.commit()
        flash("Usuário criado com sucesso!", "success")
        return redirect(url_for("admin_usuarios_list"))

    return render_template("admin/usuarios_form.html", titulo="Novo Usuário")

@app.route("/admin/usuarios/editar/<int:id>", methods=["GET", "POST"])
@login_required
@role_required("admin") # CORRIGIDO
def admin_usuarios_editar(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == "POST":
        usuario.nome = request.form["nome"]
        usuario.email = request.form["email"]
        usuario.role = request.form["role"]
        senha = request.form.get("senha")

        if senha:
            usuario.set_senha(senha)

        db.session.commit()
        flash("Usuário atualizado com sucesso!", "success")
        return redirect(url_for("admin_usuarios_list"))

    return render_template("admin/usuarios_form.html", usuario=usuario, titulo="Editar Usuário")

@app.route("/admin/usuarios/excluir/<int:id>")
@login_required
@role_required("admin") # CORRIGIDO
def admin_usuarios_excluir(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash("Usuário excluído com sucesso!", "success")
    return redirect(url_for("admin_usuarios_list"))

# --------------------------
# ROTAS DO ADMIN (VEÍCULOS)
# --------------------------

@app.route("/admin/veiculos")
@login_required
@role_required("admin", "funcionario") # CORRIGIDO
def admin_veiculos():
    veiculos = Veiculo.query.all()
    return render_template("admin/veiculos/veiculos_list.html", veiculos=veiculos)

@app.route("/admin/veiculos/novo", methods=["GET", "POST"])
@login_required
@role_required("admin", "funcionario") # CORRIGIDO
def admin_veiculos_novo():
    if request.method == "POST":
        placa = request.form["placa"]
        # Outros dados
        
        novo_veiculo = Veiculo(
            placa=placa,
            marca=request.form["marca"],
            modelo=request.form["modelo"],
            ano=request.form["ano"],
            categoria=request.form["categoria"],
            status=request.form["status"],
            preco_diaria=request.form["preco_diaria"]
        )
        db.session.add(novo_veiculo)
        db.session.commit()
        flash("Veículo criado com sucesso!", "success")
        return redirect(url_for("admin_veiculos"))

    return render_template("admin/veiculos/veiculos_form.html")


@app.route("/admin/veiculos/<int:id>/editar", methods=["GET", "POST"])
@login_required
@role_required("admin", "funcionario") # CORRIGIDO
def admin_veiculos_editar(id):
    veiculo = Veiculo.query.get_or_404(id)

    if request.method == "POST":
        veiculo.placa = request.form["placa"]
        veiculo.marca = request.form["marca"]
        veiculo.modelo = request.form["modelo"]
        veiculo.ano = request.form["ano"]
        veiculo.categoria = request.form["categoria"]
        veiculo.status = request.form["status"]
        veiculo.preco_diaria = request.form["preco_diaria"]
        
        db.session.commit()
        flash("Veículo atualizado com sucesso!", "success")
        return redirect(url_for("admin_veiculos"))

    return render_template("admin/veiculos/veiculos_form.html", veiculo=veiculo)

@app.route("/admin/veiculos/<int:id>/excluir", methods=["POST"])
@login_required
@role_required("admin", "funcionario") # CORRIGIDO
def admin_veiculos_excluir(id):
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    flash("Veículo excluído com sucesso!", "success")
    return redirect(url_for("admin_veiculos"))

# --------------------------
# ROTAS DO ADMIN (LOCAÇÕES)
# --------------------------

@app.route("/admin/locacoes")
@login_required
@role_required("admin", "funcionario") # CORRIGIDO
def admin_locacoes():
    locacoes = Locacao.query.order_by(Locacao.data_inicio.desc()).all()
    return render_template("admin/locacoes/locacoes_list.html", locacoes=locacoes)

# Adiciona rota de nova locação pelo painel
@app.route("/admin/locacoes/nova", methods=["GET", "POST"])
@login_required
@role_required("admin", "funcionario") # CORRIGIDO
def admin_locacoes_nova():
    usuarios = Usuario.query.filter_by(role="cliente").all()
    veiculos = Veiculo.query.filter_by(status="disponivel").all()

    if request.method == "POST":
        usuario_id = request.form.get("usuario_id")
        veiculo_id = request.form.get("veiculo_id")
        # Note: datas como string no POST, converter
        data_inicio_str = request.form.get("data_inicio")
        data_fim_str = request.form.get("data_fim")

        data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d')
        data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d')
        
        veiculo = Veiculo.query.get(veiculo_id)

        # Validação de Conflito de Locação (Simplificada)
        conflito_locacao = Locacao.query.filter(
            Locacao.veiculo_id == veiculo_id,
            Locacao.status.in_(["pendente", "confirmada", "ativa"]),
            Locacao.data_fim >= data_inicio,
            Locacao.data_inicio <= data_fim
        ).first()

        if conflito_locacao:
            flash("Este veículo já possui uma reserva ou locação ativa no período solicitado.", "danger")
            return redirect(url_for("admin_locacoes_nova"))

        # Cálculo do valor
        dias = (data_fim - data_inicio).days + 1 
        valor_total = dias * veiculo.preco_diaria

        nova_locacao = Locacao(
            usuario_id=usuario_id,
            veiculo_id=veiculo_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
            valor_total=valor_total,
            status="confirmada" # Locações criadas pelo admin/func são confirmadas diretamente
        )

        db.session.add(nova_locacao)
        # O veículo deve ser marcado como alugado IMEDIATAMENTE após a criação/confirmação
        veiculo.status = "alugado"
        
        db.session.commit()
        flash("Locação criada e confirmada com sucesso!", "success")
        return redirect(url_for("admin_locacoes"))

    return render_template("admin/locacoes/locacoes_form.html", usuarios=usuarios, veiculos=veiculos)


# *** CORREÇÃO: VERSÃO SEGURA E COMPLETA DA ROTA DE FINALIZAÇÃO (MANTIDA E CORRIGIDA) ***
@app.route("/admin/locacoes/<int:id>/finalizar", methods=["POST"])
@login_required
@role_required("funcionario", "admin") # CORRIGIDO
def finalizar_locacao(id):
    loc = Locacao.query.get_or_404(id)

    # Verifica se o status é passível de finalização
    if loc.status != "confirmada" and loc.status != "ativa":
        flash("A locação não pode ser finalizada neste status.", "danger")
        return redirect(url_for("admin_locacoes")) 

    # 1. Muda o status da locação para finalizada
    loc.status = "finalizada"
    
    # 2. Muda o status do veículo para 'disponivel'
    # É mais seguro buscar o veículo pela locação, se o relacionamento estiver configurado
    loc.veiculo.status = "disponivel" 
    
    db.session.commit()
    flash("Locação finalizada com sucesso! Veículo liberado para novos aluguéis.", "success")
    
    return redirect(url_for("admin_locacoes"))

# *** ROTA DUPLICADA EXCLUÍDA: A rota 'admin_locacoes_finalizar' foi removida para evitar conflitos. ***

# --------------------------
# ROTAS DO CLIENTE
# --------------------------

@app.route("/cliente")
@login_required
@role_required("cliente") # CORRIGIDO
def cliente_dashboard():
    return render_template("cliente/dashboard.html")

@app.route("/cliente/veiculos")
@login_required
@role_required("cliente") # CORRIGIDO
def cliente_lista_veiculos():
    veiculos = Veiculo.query.filter_by(status="disponivel").all()
    # Assume que o template é templates/cliente/veiculos_list.html
    return render_template("cliente/veiculos_list.html", veiculos=veiculos)

@app.route("/cliente/solicitar_locacao/<int:veiculo_id>", methods=["GET", "POST"])
@login_required
@role_required("cliente") # CORRIGIDO
def cliente_solicitar_locacao(veiculo_id):
    veiculo = Veiculo.query.get_or_404(veiculo_id)
    usuario_id = session.get("usuario_id")
    
    if request.method == "POST":
        data_inicio_str = request.form.get("data_inicio")
        data_fim_str = request.form.get("data_fim")

        # Validações de data
        try:
            data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d')
            data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d')
        except ValueError:
            flash("Formato de data inválido.", "danger")
            return redirect(url_for("cliente_solicitar_locacao", veiculo_id=veiculo_id))
        
        if data_inicio < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) or data_fim <= data_inicio:
            flash("Datas de locação inválidas.", "danger")
            return redirect(url_for("cliente_solicitar_locacao", veiculo_id=veiculo_id))

        # Validação de Conflito de Locação (Simplificada)
        conflito_locacao = Locacao.query.filter(
            Locacao.veiculo_id == veiculo_id,
            Locacao.status.in_(["pendente", "confirmada", "ativa"]),
            Locacao.data_fim >= data_inicio,
            Locacao.data_inicio <= data_fim
        ).first()

        if conflito_locacao:
            flash("Este veículo já possui uma reserva ou locação ativa no período solicitado.", "danger")
            return redirect(url_for("cliente_solicitar_locacao", veiculo_id=veiculo_id))

        # Se passou por todas as validações:
        # Incluir o dia de devolução no cálculo
        dias = (data_fim - data_inicio).days + 1 
        valor_total = dias * veiculo.preco_diaria

        nova_locacao = Locacao(
            usuario_id=usuario_id,
            veiculo_id=veiculo_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
            valor_total=valor_total,
            status="pendente" # O cliente SEMPRE gera uma solicitação 'pendente'
        )

        db.session.add(nova_locacao)
        db.session.commit()
        flash("Solicitação de locação enviada com sucesso! Aguarde a confirmação do funcionário.", "success")
        return redirect(url_for("cliente_minhas_locacoes"))

    # GET: Exibir o formulário
    return render_template("cliente/locacao_form.html", veiculo=veiculo, now=datetime.now())


@app.route("/cliente/locacoes")
@login_required
@role_required("cliente") 
def cliente_minhas_locacoes():
    usuario_id = session.get("usuario_id")
    # Busca locações do usuário, ordenadas da mais recente para a mais antiga
    locacoes = Locacao.query.filter_by(usuario_id=usuario_id).order_by(Locacao.data_inicio.desc()).all()
    return render_template("cliente/locacoes_list.html", locacoes=locacoes)

# --------------------------
# ROTAS DO FUNCIONÁRIO
# --------------------------

@app.route("/funcionario")
@login_required
@role_required("funcionario", "admin") 
def funcionario_dashboard():
    return render_template("funcionario/dashboard.html")

@app.route("/funcionario/locacoes/pendentes")
@login_required
@role_required("funcionario", "admin") 
def funcionario_locacoes_pendentes():
    pendentes = Locacao.query.filter_by(status="pendente").all()
    return render_template("funcionario/locacoes_pendentes.html", locacoes=pendentes)

@app.route("/funcionario/locacoes/<int:id>/confirmar")
@login_required
@role_required("funcionario", "admin") 
def funcionario_confirmar_locacao(id):
    loc = Locacao.query.get_or_404(id)
    loc.status = "confirmada"
    loc.veiculo.status = "alugado"
    db.session.commit()
    flash(f"Locação #{loc.id} confirmada e veículo reservado!", "success")
    return redirect(url_for("funcionario_locacoes_pendentes"))


@app.route("/funcionario/locacoes/<int:id>/rejeitar")
@login_required
@role_required("funcionario", "admin") 
def funcionario_rejeitar_locacao(id):
    loc = Locacao.query.get_or_404(id)
    loc.status = "rejeitada"
    db.session.commit()
    flash(f"Locação #{loc.id} rejeitada.", "warning")
    return redirect(url_for("funcionario_locacoes_pendentes"))

@app.route("/funcionario/veiculos")
@login_required
@role_required("funcionario", "admin")
def funcionario_lista_veiculos():
    veiculos = Veiculo.query.all()
    return render_template("admin/veiculos/veiculos_list.html", veiculos=veiculos)

@app.route("/funcionario/clientes")
@login_required
@role_required("funcionario", "admin") 
def funcionario_lista_clientes():
    clientes = Usuario.query.filter_by(role="cliente").all()
    # Assume que o template é templates/funcionario/clientes.html ou similar
    return render_template("funcionario/clientes.html", clientes=clientes)