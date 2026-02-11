# Design de Interface - AdBounty Telegram Mini App

## Visão Geral

AdBounty é um marketplace de anúncios descentralizado integrado ao Telegram, permitindo que anunciantes criem campanhas (bounties) e compensem proprietários de canais por publicação de conteúdo. O design segue iOS Human Interface Guidelines (HIG) com foco em mobile portrait (9:16) e uso com uma mão.

## Lista de Telas

1. **Splash/Onboarding** - Tela inicial com branding AdBounty
2. **Login Telegram** - Autenticação via Telegram SDK
3. **Catálogo de Canais** - Lista de canais verificados (subs/niche)
4. **Detalhes do Canal** - Informações do canal e bounties ativas
5. **Criar Bounty** - Formulário para anunciante (TON amount, texto, link, canais alvo)
6. **Meus Bounties** - Lista de bounties criadas pelo usuário
7. **Detalhes da Bounty** - Visualização completa com status e bids
8. **Bid/Escrow** - Confirmação de depósito TON Connect
9. **Meus Deals** - Lista de deals aceitos (owner)
10. **Confirmação de Views** - Owner confirma visualizações para release de payout
11. **Histórico de Transações** - Registro de todas as transações TON
12. **Perfil/Configurações** - Dados do usuário e preferências

## Fluxo Primário: 1 Bounty Completa

### Fluxo do Anunciante (Advertiser)
1. **Login** → Telegram OAuth → Acesso ao app
2. **Criar Bounty** → Form: TON amount, ad text/link, target channels
3. **Confirmar & Pagar** → TON Connect deposit em vault testnet
4. **Aguardar** → Backend confirma e Bot.sendMessage no canal
5. **Visualizar Status** → Meus Bounties mostra status "Posted"

### Fluxo do Proprietário de Canal (Channel Owner)
1. **Login** → Telegram OAuth → Acesso ao app
2. **Catálogo** → Lista canais verificados que possui
3. **Ver Bounties** → Detalhes do Canal mostra bounties disponíveis
4. **Aceitar Bid** → Confirma aceitação da bounty
5. **Receber Anúncio** → Bot publica no canal automaticamente
6. **Confirmar Views** → Owner confirma que anúncio foi visualizado
7. **Receber Payout** → Smart contract libera TON para owner

## Conteúdo Primário por Tela

### Splash/Onboarding
- Logo AdBounty (ícone + texto)
- Tagline: "Monetize Your Channel"
- Botão: "Login with Telegram"

### Login Telegram
- Campo de entrada para Telegram ID (ou QR code)
- Botão "Connect Telegram Account"
- Status de autenticação

### Catálogo de Canais
- SearchBar para filtrar canais
- Lista de cards com:
  - Ícone/foto do canal
  - Nome do canal
  - Número de subscribers
  - Niche/categoria
  - Badge "Verified" se aplicável
  - Botão "View Details"

### Detalhes do Canal
- Header: foto do canal, nome, subs, niche
- Seção "Active Bounties":
  - Cards com bounties disponíveis
  - Cada card mostra: TON amount, ad text preview, deadline
  - Botão "Bid on This"
- Seção "Your Stats" (se é owner):
  - Total earnings
  - Active deals
  - Completed deals

### Criar Bounty (Form)
- Input: TON amount (slider ou input numérico)
- Input: Ad text (textarea, max 280 chars)
- Input: Ad link (URL)
- Multi-select: Target channels
- Input: Deadline (date picker)
- Botão: "Review & Pay"

### Meus Bounties
- Abas: "Active" | "Completed" | "Cancelled"
- Lista de bounties com status:
  - "Pending Payment" (amarelo)
  - "Posted" (verde)
  - "Completed" (cinza)
- Cada item mostra: title, TON amount, target channels, status
- Botão de detalhes para cada bounty

### Detalhes da Bounty
- Header: TON amount, status badge
- Seção "Ad Content": texto e link
- Seção "Target Channels": lista dos canais
- Seção "Bids": lista de channel owners que fizeram bid
  - Cada bid mostra: channel name, owner name, status
  - Botão "Accept" (se pending)
  - Botão "View Proof" (se completed)

### Bid/Escrow (TON Connect)
- Resumo da transação:
  - Bounty title
  - TON amount
  - Gas fee estimate
- Botão: "Connect TON Wallet"
- Botão: "Confirm Payment"
- Status: "Processing..." → "Success" ou "Error"

### Meus Deals (Owner)
- Abas: "Active" | "Completed"
- Lista de deals aceitos:
  - Bounty title, advertiser name, TON amount, status
  - Status: "Posted" (verde) | "Awaiting Confirmation" (amarelo)
  - Botão "Confirm Views" (se status = Posted)

### Confirmação de Views
- Resumo do deal
- Checkbox: "I confirm this ad was posted and viewed"
- Foto/screenshot opcional
- Botão: "Confirm & Release Payout"
- Status: "Processing..." → "Payout Released"

### Histórico de Transações
- Lista de todas as transações TON:
  - Data, tipo (deposit/payout), amount, status
  - Link para explorador TON testnet
- Filtro: "All" | "Deposits" | "Payouts"

### Perfil/Configurações
- Dados do usuário:
  - Telegram ID
  - Wallet address (TON)
  - Total earned (lifetime)
  - Total spent (lifetime)
- Preferências:
  - Notificações on/off
  - Tema (light/dark)
  - Idioma (EN/PT-BR)
- Botão: "Logout"

## Cores da Marca

- **Primary**: #0A7EA4 (Azul TON)
- **Secondary**: #1F97E6 (Azul claro)
- **Success**: #22C55E (Verde)
- **Warning**: #F59E0B (Âmbar)
- **Error**: #EF4444 (Vermelho)
- **Background**: #FFFFFF (Light) / #151718 (Dark)
- **Surface**: #F5F5F5 (Light) / #1E2022 (Dark)
- **Foreground**: #11181C (Light) / #ECEDEE (Dark)
- **Muted**: #687076 (Light) / #9BA1A6 (Dark)

## Padrões de Interação

- **Botões primários**: Azul TON, corner radius 12px, altura 48px
- **Cards**: Background surface, border subtle, corner radius 16px
- **Listas**: ScrollView com FlatList, pull-to-refresh
- **Modais**: Bottom sheet para confirmações
- **Feedback**: Toast notifications para ações (sucesso/erro)
- **Haptics**: Light feedback em botões, Medium em confirmações críticas

## Considerações Técnicas

- Integração com Telegram SDK para autenticação
- TON Connect para wallet integration
- Suporte a testnet TON
- Responsivo para todos os tamanhos de tela mobile
- Suporte a dark mode
- Offline-first com sincronização quando online
