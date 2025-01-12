#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `Adobe Acrobat Reader DC (Wine)` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `Adobe Acrobat Reader DC (Wine)` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/use Adobe `Acrobat Reader DC (Wine)` on `Linux Ubuntu`._

# ## Descrição
# 
# ### `Adobe Acrobat Reader DC` [2]
# 
# O `Adobe Acrobat Reader DC` é um dos leitores de PDF mais populares e amplamente utilizados do mundo. Desenvolvido pela Adobe, ele oferece uma ampla gama de recursos para visualizar, imprimir, comentar e assinar documentos em formato PDF. O `Adobe Acrobat Reader DC` permite abrir e ler documentos PDF em vários dispositivos e sistemas operacionais, oferecendo uma experiência consistente de leitura e interação. Além disso, ele suporta recursos avançados, como preenchimento de formulários interativos e assinaturas eletrônicas, tornando-o uma escolha essencial para profissionais que lidam com documentos PDF em suas atividades diárias. Com sua interface amigável e recursos robustos, o Acrobat Reader DC é amplamente adotado em ambientes de negócios, educação e governamentais para visualizar e gerenciar documentos PDF com eficiência.
# 

# ## 1. Configurar/Instalar/Usar o `Adobe Acrobat Reader DC (Wine)` no `Linux Ubuntu` [1]
# 
# Para instalar o `Adobe Acrobat Reader DC (Wine)`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# O `Adobe Acrobat Reader DC` pode ser instalado em todas as versões atualmente suportadas do `Linux Ubuntu` instalando o pacote `snap acrordrdc`. [3]
# 
# 3. **`Instale o `Snapd``:** O `snapd` é o serviço que permite instalar e gerenciar Snaps. Instale-o com o seguinte comando: `sudo apt install snapd`
# 
# 4. **`Ative o `Snapd``:** Depois de instalar o `snapd`, é necessário ativá-lo. Você pode fazer isso com o seguinte comando: `sudo systemctl enable --now snapd apparmor`
# 
# 5. **Instale o pacote snap acrordrdc:** `sudo snap install acrordrdc`
# 
# 6. **Inicie o `acrordrdc`:** `acrordrdc`
# 
# 7. As mensagens de configuração serão mostradas no terminal enquanto o Wine está configurando para o Adobe Reader. Aguarde o Wine terminar a configuração do Adobe Reader. Após a configuração do Wine, você verá um ícone vermelho do Adobe Reader no Dock e esta janela será aberta.
# 
#     <div align="center">
#         <img src="figures/fig1.png" alt="Minha Imagem" />
#         <p>Fig. 1 .</p>
#     </div>
# 
# 8. Selecione um idioma para download do instalador no menu suspenso e clique no botão Instalar na janela do Adobe Acrobat Reader DC. Uma pequena janela da barra de progresso será aberta para mostrar o progresso do download do Adobe Acrobat Reader DC.
# 
# 9. Inicie o Adobe Acrobat Reader DC. Um ícone vermelho do Adobe Reader aparecerá no Dock quando o Adobe Acrobat Reader DC estiver aberto: `acrordrdc`
# 
# 10. Pode ser necessário desativar o Modo Protegido (_Protect Mode_) para abrir o Adobe Acrobat Reader DC, ou seja, selecione a opção `Open with Protect Mode disabled`.
#     
#     10.1 Em caso afirmativo, selecione a opção: `Open with Protect Mode disabled`;
# 
#     10.2 Clique em: `OK`
# 
#     <div align="center">
#         <img src="figures/fig2.png" alt="Minha Imagem" />
#         <p>Fig. 2 .</p>
#     </div> 
# 
# 11. Pressione o botão `Accept` para aceitar o Contrato de Licença do Adobe Acrobat Reader DC e continuar.
# 
#     <div align="center">
#         <img src="figures/fig3.png" alt="Minha Imagem" />
#         <p>Fig. 3 .</p>
#     </div> 
# 
# 12. Você pode preencher formulários automaticamente se fizer login no Adobe Acrobat Reader DC, conforme mostrado no canto superior direito da captura de tela abaixo.
# 
#     <div align="center">
#         <img src="figures/fig4.png" alt="Minha Imagem" />
#         <p>Fig. 4 .</p>
#     </div> 
# 
# 13. Minha versão atual do Adobe Acrobat Reader DC é `21.007.20091.59174`, a versão mais recente. Pode ser necessário reinstalar o pacote snap acrordrdc se você atualizar sua versão do Ubuntu para garantir que ele seja compatível com seu sistema operacional atualizado.
# 
#     <div align="center">
#         <img src="figures/fig5.png" alt="Minha Imagem" />
#         <p>Fig. 5 .</p>
#     </div> 
# 

# ## 2. Código completo para a configuração/instalação/usar
# 
# Para instalar o `Adobe Acrobat Reader DC (Wine)` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                                                            
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install snapd
#     sudo systemctl enable --now snapd apparmor
#     sudo snap install acrordrdc
#     acrordrdc
#     ```
# 

# ## Referências
# 
# [1] USER1051028. ***Adobe reader 9 and adobe acrobat reader dc (wine).*** Disponível em: <https://askubuntu.com/questions/1371236/adobe-reader-9-and-adobe-acrobat-reader-dc-wine> (texto adaptado). Ask Ubuntu. Acessado em: 23/11/2023 15:53.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 23/11/2023 15:53.
# 
# [3] OPENAI. ***Instale o snapd no kali:*** Disponível em: <https://chat.openai.com/c/de1dd3d6-e628-489e-9d6b-8c1093c97742> (texto adaptado). ChatGPT. Acessado em: 29/11/2023 22:08.
# 
