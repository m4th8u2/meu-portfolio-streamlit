

# --- CONFIGURAÇÃO DA PÁGINA ---
# st.set_page_config deve ser o primeiro comando Streamlit
st.set_page_config(
    page_title="Estrutura, Transformação e Fé",
    page_icon="✨",
    layout="wide",
)

# --- FUNÇÕES PARA CADA PÁGINA ---

def pagina_inicio():
    """Página de introdução com o conceito principal e as imagens geradas."""
    st.title("Estrutura, Transformação e Fé ✨")
    st.markdown("---")
    st.markdown("### Uma jornada conceitual através da Tecnologia, Arte e Espiritualidade.")
    st.write("""
    Bem-vindo! Este espaço explora as conexões surpreendentes entre três mundos aparentemente distintos: 
    a **Tecnologia da Informação**, a arte do **Origami** e a **Religião Católica**. 
    Vamos descobrir como os temas de **estrutura, processo e transformação** formam a base de cada um, 
    revelando a beleza que emerge da complexidade.
    """)
    st.markdown("---")

    # Seção 1: TI
    col1, col2 = st.columns([1, 2])
    with col1:
        # IMPORTANTE: Substitua a URL abaixo pela sua imagem de TI!
        # Pode ser um link ou um arquivo local, ex: st.image("imagens/ti.jpg")
        st.image(
            "TI.jpg",
            caption="A arquitetura da lógica digital."
        )
    with col2:
        st.subheader("1. TI: A Arquitetura da Lógica")
        st.write("""
        No coração da Tecnologia da Informação existe uma estrutura invisível, mas profundamente ordenada. 
        Algoritmos, como receitas precisas, ditam o comportamento de sistemas complexos. 
        A TI nos mostra que a partir de regras lógicas simples (zeros e uns), podemos construir universos 
        de complexidade infinita.
        """)

    st.markdown("---")

    # Seção 2: Origami
    col3, col4 = st.columns([2, 1])
    with col3:
        st.subheader("2. Origami: A Transformação do Plano")
        st.write("""
        O Origami é a arte de transformar o simples no sublime. Uma única folha de papel passa por um 
        processo de dobras precisas e sequenciais. Cada dobra é um passo em um algoritmo sagrado que, 
        quando seguido com cuidado, transforma o caos potencial em forma e significado.
        """)
    with col4:
        # IMPORTANTE: Substitua pela sua imagem de Origami!
        st.image(
            "Origami.jpg",
            caption="A transformação do plano em forma."
        )
        
    st.markdown("---")

    # Seção 3: Religião Católica
    col5, col6 = st.columns([1, 2])
    with col5:
        # IMPORTANTE: Substitua pela sua imagem da Catedral!
        st.image(
            "Igreja.jpg",
            caption="A estrutura que eleva a fé."
        )
    with col6:
        st.subheader("3. Religião Católica: A Estrutura da Fé")
        st.write("""
        A fé, embora profundamente pessoal, também se manifesta através de uma estrutura. A liturgia, 
        os rituais e os sacramentos fornecem um caminho ordenado para a transformação espiritual. 
        A estrutura não limita a fé, mas serve como o vaso que a contém, permitindo a conexão com o divino.
        """)


def pagina_ti():
    """Página de conteúdo detalhado sobre Tecnologia da Informação."""
    st.title("💻 Tecnologia da Informação")
    st.header("A Arquitetura da Lógica")
    
    st.markdown("""
    A Tecnologia da Informação (TI) é a espinha dorsal da sociedade moderna. Ela representa o vasto conjunto de soluções, processos e ferramentas usados para criar, armazenar, gerenciar e disseminar informação. Mais do que apenas computadores e softwares, a TI é a materialização da lógica humana, uma arquitetura complexa que transformou a maneira como vivemos, trabalhamos e nos comunicamos, permitindo que dados brutos se tornem conhecimento valioso.

    ### História e Evolução
    A jornada da TI começou muito antes do smartphone no seu bolso. Podemos dividi-la em eras distintas:
    - **Década de 1960 (A Era do Processamento de Dados):** O marco inicial, com computadores gigantes (mainframes) que ocupavam salas inteiras. 
    - **Década de 1970 (A Era dos Sistemas de Informação):** Surgiram os primeiros Sistemas de Gerenciamento de Banco de Dados (SGBDs), permitindo um acesso mais estruturado à informação.
    - **Década de 1980 (A Era da Vantagem Competitiva):** A chegada dos computadores pessoais (PCs) democratizou o acesso à tecnologia.
    - **Década de 1990 em diante (A Era da Integração e da Internet):** A popularização da internet conectou o mundo. Hoje, vivemos na era da computação em nuvem (Cloud Computing), Inteligência Artificial (IA) e Internet das Coisas (IoT).

    ### Conceitos e Fundamentos
    A TI se apoia em quatro pilares fundamentais:
    1.  **Hardware:** A parte física (computadores, servidores, smartphones).
    2.  **Software:** A parte lógica (programas, aplicativos, sistemas operacionais).
    3.  **Banco de Dados:** Sistemas organizados para armazenar e recuperar grandes volumes de dados.
    4.  **Redes:** A infraestrutura que permite a comunicação, como a internet.
    """)


def pagina_origami():
    """Página de conteúdo detalhado sobre Origami."""
    st.title("🦢 Origami")
    st.header("A Transformação do Plano")

    st.markdown("""
    Origami (do japonês *ori*, "dobrar", e *kami*, "papel") é a arte milenar de criar representações de seres ou objetos através da dobradura de uma única folha de papel, sem cortes ou colagem. É uma manifestação artística que celebra a transformação: o poder de um processo ordenado e preciso para converter uma superfície plana e bidimensional em uma escultura tridimensional cheia de vida e significado.

    ### História e Evolução
    Embora o papel tenha sido inventado na China, foi no Japão que a arte de dobrá-lo floresceu.
    - **Origens (Século VI):** Seu uso era restrito a cerimônias religiosas e rituais da nobreza, como oferendas ou símbolos de boa sorte.
    - **Período Edo (1603-1868):** O origami se espalhou por toda a sociedade japonesa, tornando-se uma forma de lazer e educação.
    - **Era Moderna (Século XX):** O mestre **Akira Yoshizawa** é considerado o "pai do origami moderno". Ele elevou a dobradura ao status de arte e desenvolveu o sistema de diagramas usado até hoje.

    ### Conceitos e Fundamentos
    A essência do origami reside na sua simplicidade de regras e na complexidade de resultados.
    - **A Folha Quadrada:** Simboliza um mundo de possibilidades contido em uma forma perfeita.
    - **Dobras Fundamentais:** Todas as criações são combinações de dobras básicas, como "vale" e "montanha".
    - **Simbolismo:** O **Tsuru (grou)** é o mais icônico, simbolizando paz, saúde e longevidade. Uma lenda diz que aquele que dobrar mil tsurus terá um desejo atendido.
    """)


def pagina_catolica():
    """Página de conteúdo detalhado sobre a Religião Católica."""
    st.title("🕊️ Religião Católica")
    st.header("A Estrutura da Fé")

    st.markdown("""
    O Catolicismo é uma das maiores e mais antigas instituições do mundo, uma fé cristã que se baseia nos ensinamentos de Jesus Cristo. Sua doutrina se desenvolveu ao longo de dois milênios, criando uma rica tapeçaria de teologia, tradição e rituais. Para os católicos, a Igreja é mais do que um lugar; é uma comunidade global unida por uma estrutura de crenças, sacramentos e liderança que visa guiar os fiéis em sua jornada espiritual.

    ### História e Evolução
    A história da Igreja Católica é intrinsecamente ligada à história do Ocidente.
    - **Fundação (Século I):** A tradição sustenta que a Igreja foi fundada por Jesus Cristo, que conferiu a liderança ao apóstolo Pedro, considerado o primeiro Papa.
    - **Idade Média e Renascença:** A Igreja desempenhou um papel central na sociedade medieval, preservando a cultura clássica e fundando as primeiras universidades.
    - **Reforma e Contrarreforma (Século XVI):** A Reforma Protestante levou a uma cisão na cristandade. A Igreja Católica respondeu com a Contrarreforma, reafirmando seus dogmas no Concílio de Trento.

    ### Doutrinas e Fundamentos
    A fé católica é baseada na Bíblia e na Tradição Apostólica. As crenças centrais incluem:
    1.  **A Santíssima Trindade:** A crença em um só Deus em três Pessoas distintas: Pai, Filho e Espírito Santo.
    2.  **Os Sete Sacramentos:** Ritos sagrados considerados canais da graça de Deus (Batismo, Eucaristia, Crisma, etc.).
    3.  **A Eucaristia:** A crença central de que o pão e o vinho consagrados se tornam o Corpo e Sangue de Cristo.
    4.  **A Sucessão Apostólica:** A crença de que o Papa e os bispos são os sucessores dos apóstolos.
    """)


# --- NAVEGAÇÃO PRINCIPAL ---

# Dicionário de páginas
paginas = {
    "Início": pagina_inicio,
    "Tecnologia da Informação": pagina_ti,
    "Origami": pagina_origami,
    "Religião Católica": pagina_catolica,
}

# Cria a barra lateral de navegação
st.sidebar.title("Navegação")
selecao = st.sidebar.radio("Ir para", list(paginas.keys()))

# Executa a função da página selecionada
paginas[selecao]()

# Pequeno rodapé na barra lateral
st.sidebar.markdown("---")
st.sidebar.info("Site conceitual criado com Streamlit e IA.")
