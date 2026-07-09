# 🏋️ Gym API

API REST para gerenciamento de academias, desenvolvida com **Python**, **Django** e **Django REST Framework**, com foco em arquitetura backend, modelagem de domínio e boas práticas de desenvolvimento.

## 📌 Objetivo

O projeto foi desenvolvido para aprofundar conhecimentos em desenvolvimento de APIs REST, modelagem de banco de dados, regras de negócio e arquitetura backend utilizando o ecossistema Django.

---

## 🚀 Tecnologias

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- Django ORM
- Docker *(Em desenvolvimento)*
- JWT *(Em desenvolvimento)*
- Stripe *(Em desenvolvimento)*

---

## 🏗️ Arquitetura

O projeto foi organizado em módulos independentes seguindo o princípio de separação de responsabilidades.

```text
gym_api/
│
├── accounts/
│   ├── User
│   └── Profile
│
├── academy/
│   ├── Membership
│   ├── Exercise
│   ├── Workout
│   └── WorkoutExercise
│
└── gym_api/
```

---

## 📊 Modelagem do domínio

```text
User
 │
 ▼
Profile
 │
 ▼
Membership
 │
 ▼
Workout
 │
 ▼
WorkoutExercise
 │
 ▼
Exercise
```

---

## ⚙️ Funcionalidades

- ✅ Custom User com autenticação por e-mail
- ✅ Controle de perfis (Administrador, Personal e Aluno)
- ✅ Gerenciamento de matrículas
- ✅ Cadastro de exercícios por grupo muscular
- ✅ Criação de planos de treino
- ✅ Configuração de séries, repetições e descanso
- ✅ Organização dos exercícios por ordem de execução
- ✅ Django Admin personalizado
- 🔄 API REST com Django REST Framework
- 🔄 Autenticação JWT
- 🔄 Integração com Stripe

---

## 📋 Regras de negócio

- Cada usuário possui apenas um perfil.
- Um aluno possui apenas uma matrícula ativa.
- A matrícula controla o vínculo do aluno com a academia.
- Personais podem criar treinos para seus alunos.
- Um treino pode conter vários exercícios.
- O mesmo exercício pode ser reutilizado em diferentes treinos.
- Cada exercício do treino possui séries, repetições, descanso e ordem de execução.
- Exercícios e matrículas podem ser ativados ou desativados sem perda do histórico.

---

## 💡 Conceitos aplicados

- Django ORM
- Modelagem de domínio
- Relacionamentos OneToOne e ForeignKey
- Custom User
- TextChoices
- Django Admin personalizado
- Organização modular por apps
- Separação de responsabilidades
- Boas práticas de arquitetura backend

---

## 📈 Roadmap

- [x] Modelagem do banco de dados
- [x] Custom User
- [x] Profile
- [x] Membership
- [x] Exercise
- [x] Workout
- [x] WorkoutExercise
- [ ] API REST
- [ ] Serializers
- [ ] ViewSets
- [ ] JWT Authentication
- [ ] Permissions
- [ ] Pagination
- [ ] Filters
- [ ] Docker
- [ ] Stripe
- [ ] Testes automatizados

---

## 👨‍💻 Autor

**Marcelo Costa**

- GitHub: https://github.com/SenhorDosSonhos
- LinkedIn: https://linkedin.com/in/marcelo-dev-br