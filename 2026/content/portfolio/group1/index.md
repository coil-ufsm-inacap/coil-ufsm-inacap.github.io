+++
title = "EcoAvanza · Grupo 1"
weight = 1
group = 1
draft = false
image = "cover.jpg"
description = "Diagnóstico de sostenibilidad con perfil de empresa, resultados y plan de acciones."
application = "https://project3-2026b-gabriel-maroneze-oropoc.onrender.com/"
repository = "https://github.com/elc1090/project3-2026b-gabriel-maroneze-oropoc"
+++

🇧🇷 A aplicação reúne cadastro de empresas, questionário de diagnóstico, visualização de resultados e organização de ações de sustentabilidade. A interface combina páginas renderizadas no servidor com requisições JavaScript às rotas de dados.

🇨🇱 La aplicación reúne registro de empresas, cuestionario de diagnóstico, visualización de resultados y organización de acciones de sostenibilidad. La interfaz combina páginas renderizadas en el servidor con solicitudes JavaScript a las rutas de datos.

{{< demo src="demo.gif" caption="Demonstração da equipe / Demostración del equipo" >}}

## Acesso / Acceso

{{< project-links >}}

## Equipe / Equipo

### Brasil · UFSM

- Gabriel Maroneze Ramos
- João Daniel Wurdig Lucas

### Chile · INACAP

- Vicenta Dodds
- Valentina García

## Tecnologias / Tecnologías

| Camada / Capa | Implementação / Implementación |
|---|---|
| Interface / Interfaz | HTML, CSS, JavaScript; templates Jinja2 |
| Servidor | Python, FastAPI, Pydantic |
| Persistência / Persistencia | PostgreSQL; Psycopg |
| Autenticação / Autenticación | Cookie de sessão assinado / Cookie de sesión firmado (Starlette); hash Argon2 com pwdlib |
| Hospedagem / Alojamiento | Render; Docker |
