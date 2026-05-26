from pathlib import Path


root = Path(r"c:\Users\Pichau\Documents\harryninja.github.io")
blog_dir = root / "blog-posts"
index_path = root / "index.html"


articles = [
    {
        "file": "blog-1.html",
        "category": "GitHub",
        "date": "17/08/2023",
        "read_time": "4 min",
        "card_title": "README do GitHub como vitrine",
        "title": "Como eu uso o README do GitHub como vitrine profissional",
        "description": "Como transformar o README do GitHub em uma vitrine profissional alinhada a projetos full-stack, cloud, web3 e games.",
        "cover": "../images/blogs/readmegit/readmegit.png",
        "card_cover": "images/blogs/readmegit/readmegit.png",
        "lead": "Com uma carreira espalhada entre full-stack, DevSecOps, cloud, web3, mobile e games, eu aprendi que o README do perfil no GitHub precisa ser simples, direto e mostrar contexto rapido.",
        "summary": "Um guia pratico para usar o README do GitHub como apresentacao tecnica e profissional.",
        "content": """
            <h2>Por que eu valorizo tanto essa pagina</h2>
            <p>Meu GitHub nao serve so para guardar codigo. Ele funciona como uma vitrine de quem eu sou como desenvolvedor. Como ja trabalhei com Node.js, Python, React, Angular, cloud, Unity e web3, o README me ajuda a organizar essa identidade para quem chega no meu perfil pela primeira vez.</p>
            <h2>O que eu considero essencial</h2>
            <ul>
                <li>Uma bio curta com area principal de atuacao.</li>
                <li>Stacks em que realmente tenho vivencia profissional ou pratica consistente.</li>
                <li>Links para portfolio, LinkedIn e projetos que representam meu trabalho.</li>
                <li>Separacao clara entre o que eu uso no dia a dia e o que estudo por interesse.</li>
            </ul>
            <h2>O que eu evito</h2>
            <ul>
                <li>Excesso de badges sem contexto.</li>
                <li>Visual poluido so para parecer bonito.</li>
                <li>Listas gigantescas de tecnologias que nao contam uma historia.</li>
            </ul>
            <blockquote>O melhor README de perfil nao e o mais carregado. E o que deixa claro em poucos segundos o que voce sabe construir e em que tipo de problema consegue ajudar.</blockquote>
            <h2>Como eu penso a estrutura</h2>
            <p>Normalmente eu separo em resumo profissional, stacks principais, areas de interesse e links diretos. Como meu historico mistura produto, plataforma, cloud e games, tento deixar isso visivel sem parecer uma lista aleatoria.</p>
            <p>Se quiser olhar referencias, vale ver <a href="https://github.com/cubos-academy/academy-template-readme-profile" target="_blank" rel="noreferrer">este template</a> e tambem <a href="https://github.com/harryninja/harryninja/blob/master/README.md?plain=1" target="_blank" rel="noreferrer">meu README atual</a>.</p>
        """,
    },
    {
        "file": "blog-2.html",
        "category": "Ferramentas",
        "date": "17/08/2023",
        "read_time": "5 min",
        "card_title": "Extensoes de VSCode",
        "title": "Extensoes de VSCode que combinam com minha rotina",
        "description": "Extensoes de VSCode que fazem sentido para uma rotina que mistura full-stack, cloud, web3, Unity e produtividade.",
        "cover": "../images/blogs/vscodeext/vscode.png",
        "card_cover": "images/blogs/vscodeext/vscode.png",
        "lead": "Como eu alterno entre backend, frontend, cloud, scripts, web3 e ate projetos em Unity, meu VSCode virou uma ferramenta central. O segredo foi montar um conjunto enxuto de extensoes que realmente ajudam.",
        "summary": "Minha selecao pessoal de extensoes para uma rotina tecnica bem variada.",
        "content": """
            <h2>Meu criterio para instalar extensoes</h2>
            <p>Eu so mantenho extensoes que melhoram leitura, navegacao, debug ou produtividade. Quando a IDE fica pesada ou poluida demais, o ganho desaparece.</p>
            <h2>As que fazem mais sentido no meu dia a dia</h2>
            <ul>
                <li><strong>Docker</strong> para inspecionar containers e imagens com mais rapidez.</li>
                <li><strong>Error Lens</strong> para deixar erros e avisos muito mais visiveis.</li>
                <li><strong>Git Graph</strong> e <strong>Git History</strong> para navegar melhor no historico.</li>
                <li><strong>C#</strong> e <strong>C# Dev Kit</strong> quando estou mexendo com Unity ou .NET.</li>
                <li><strong>Prisma</strong>, <strong>Solidity</strong> e snippets especificos quando o projeto pede.</li>
                <li><strong>WakaTime</strong> para observar quanto tempo estou dedicando por contexto tecnico.</li>
            </ul>
            <h2>Por que isso conversa com minha experiencia</h2>
            <p>Como ja trabalhei com Node.js, Flask, Angular, React, C#, Solidity, infraestrutura e testes, eu preciso de uma IDE que acompanhe bem essa mudanca de contexto. Por isso dou mais valor para navegacao, leitura e feedback rapido do que para efeitos visuais.</p>
            <h2>Temas e conforto visual</h2>
            <p>Gosto de temas que ajudem a passar muito tempo codando sem cansar. Entre os que eu mais curto estao City Lights, Cyberpunk Theme, 2077 Theme e Material Icon Theme.</p>
            <div class="article-inline-image">
                <img src="../images/blogs/vscodeext/vscode2.png" alt="Painel de extensoes do VSCode">
            </div>
        """,
    },
    {
        "file": "blog-3.html",
        "category": "Games",
        "date": "17/08/2023",
        "read_time": "6 min",
        "card_title": "Unity ou Unreal",
        "title": "Unity ou Unreal: minha visao com experiencia pratica",
        "description": "Comparativo entre Unity e Unreal a partir de uma vivencia mais pratica com prototipos, estudos e projetos ligados a games.",
        "cover": "../images/blogs/unrealvsunity/unrealvsunity.webp",
        "card_cover": "images/blogs/unrealvsunity/unrealvsunity.webp",
        "lead": "Eu gosto das duas engines, mas minha relacao com Unity sempre foi mais proxima. Como ja passei por projetos e estudos em desenvolvimento de jogos, acabei formando uma opiniao mais pragmatica sobre quando cada uma faz sentido.",
        "summary": "Uma leitura pratica sobre Unity e Unreal baseada em experiencia real e perfil de projeto.",
        "content": """
            <h2>Onde Unity me ganhou</h2>
            <p>Unity sempre me pareceu uma escolha mais rapida para tirar ideia do papel. Para quem quer estudar gameplay, UI, fisica 2D, mobile ou prototipos menores, ela me parece muito eficiente.</p>
            <ul>
                <li>C# encaixa bem para quem ja tem base em desenvolvimento tradicional.</li>
                <li>O fluxo de prototipacao costuma ser mais direto.</li>
                <li>Existe muito material bom para jogos pequenos e medios.</li>
                <li>Para quem quer estudar e finalizar projetos, a curva me parece mais amigavel.</li>
            </ul>
            <h2>Quando Unreal chama atencao</h2>
            <p>Unreal me chama mais pelo peso visual e pela robustez em 3D. Quando a meta e mirar algo mais cinematografico ou com ambicao grafica maior, ela brilha.</p>
            <ul>
                <li>Ferramentas visuais fortes para prototipacao.</li>
                <li>Pipeline excelente para experiencias mais pesadas.</li>
                <li>Qualidade grafica impressionante em 3D.</li>
            </ul>
            <h2>Minha conclusao sincera</h2>
            <p>Para o tipo de projeto que mais gosto de iniciar sozinho, estudar ou iterar rapido, Unity costuma funcionar melhor para mim. Unreal continua sendo uma ferramenta muito forte, mas eu costumo enxergar Unity como a melhor porta de entrada para construir e terminar jogos menores.</p>
            <blockquote>A melhor engine quase sempre e a que te ajuda a terminar o jogo, aprender com o processo e seguir para o proximo projeto com mais maturidade.</blockquote>
        """,
    },
    {
        "file": "blog-6.html",
        "category": "Videos",
        "date": "18/08/2023",
        "read_time": "3 min",
        "card_title": "Canais de GameDev",
        "title": "Canais de GameDev que alimentam meu lado criativo",
        "description": "Uma selecao de canais de GameDev que ajudam a estudar gameplay, design, pipeline e prototipacao com mais consistencia.",
        "cover": "../images/blogs/youtubeGameDev/youtubeGameDev.jpg",
        "card_cover": "images/blogs/youtubeGameDev/youtubeGameDev.jpg",
        "lead": "Mesmo trabalhando com web, cloud e backend, eu continuo estudando game development porque isso tambem melhora minha forma de pensar produto, feedback visual, loop de interacao e experiencia do usuario.",
        "summary": "Uma lista de canais que acompanham meu estudo continuo em desenvolvimento de jogos.",
        "content": """
            <h2>Por que eu acompanho esse tipo de conteudo</h2>
            <p>GameDev mistura logica, iteracao, criatividade e feedback de forma muito intensa. Sempre que estudo jogos, sinto que isso volta para meu trabalho em software como uma melhora de sensibilidade para fluxo, clareza e experiencia de uso.</p>
            <h2>Canais que eu realmente gosto</h2>
            <ul>
                <li><a href="https://www.youtube.com/@CrieSeusJogos" target="_blank" rel="noreferrer">Crie Seus Jogos</a></li>
                <li><a href="https://www.youtube.com/@GregDevStuff" target="_blank" rel="noreferrer">GregDevStuff</a></li>
                <li><a href="https://www.youtube.com/@oprogramadordejogos" target="_blank" rel="noreferrer">O Programador de Jogos</a></li>
                <li><a href="https://www.youtube.com/@iHeartGameDev" target="_blank" rel="noreferrer">iHeartGameDev</a></li>
                <li><a href="https://www.youtube.com/@GameDevGuide" target="_blank" rel="noreferrer">GameDevGuide</a></li>
                <li><a href="https://www.youtube.com/@GMTK" target="_blank" rel="noreferrer">GMTK</a></li>
                <li><a href="https://www.youtube.com/@Brackeys" target="_blank" rel="noreferrer">Brackeys</a></li>
            </ul>
            <h2>Como eu transformo isso em aprendizado</h2>
            <p>Eu tento nao assistir so por entretenimento. Sempre que algo me chama atencao, recrio a mecanica, testo uma variacao ou aplico a ideia em um prototipo pequeno. Isso faz muito mais diferenca do que acumular tutorial visto.</p>
        """,
    },
    {
        "file": "blog-7.html",
        "category": "Mobile",
        "date": "26/05/2026",
        "read_time": "8 min",
        "card_title": "Deploy na Play Store",
        "title": "Deploy na Play Store: o que eu priorizo depois de trabalhar com mobile",
        "description": "Um guia mais pratico sobre deploy na Play Store, conectando build, assinatura, ficha da loja, testes e manutencao de release.",
        "cover": "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=modern%20mobile%20app%20release%20dashboard%20on%20laptop%20and%20smartphone%2C%20app%20publishing%20workflow%2C%20developer%20desk%2C%20dark%20blue%20and%20gold%20palette%2C%20professional%20tech%20tutorial%20cover%2C%20realistic%20lighting%2C%20clean%20composition%2C%20no%20text&image_size=landscape_16_9",
        "card_cover": "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=modern%20mobile%20app%20release%20dashboard%20on%20laptop%20and%20smartphone%2C%20app%20publishing%20workflow%2C%20developer%20desk%2C%20dark%20blue%20and%20gold%20palette%2C%20professional%20tech%20tutorial%20cover%2C%20realistic%20lighting%2C%20clean%20composition%2C%20no%20text&image_size=landscape_16_9",
        "lead": "Quando voce ja passou por desenvolvimento mobile e por ciclos reais de entrega, publicar um app deixa de ser so um passo tecnico. Vira um processo que mistura build confiavel, ficha da loja, politica de dados e manutencao futura.",
        "summary": "Checklist de publicacao na Play Store com foco em entrega limpa, manutencao e menos retrabalho.",
        "content": """
            <h2>Por que esse tema conversa comigo</h2>
            <p>Na minha trajetoria eu ja trabalhei com mobile usando Ionic Angular, backend em Node.js e integracoes ligadas a produto real. Isso me fez olhar para deploy como parte da engenharia do produto, nao como uma tarefa isolada no fim do projeto.</p>
            <h2>O que eu considero antes da release</h2>
            <ul>
                <li>Versionamento coerente e historico de release organizado.</li>
                <li>Permissoes realmente necessarias e justificadas.</li>
                <li>Descricao da loja alinhada ao comportamento real do app.</li>
                <li>Capturas de tela que explicam valor, e nao so mostram telas soltas.</li>
                <li>Politica de privacidade pronta quando ha coleta de dados.</li>
            </ul>
            <h2>Build de release do jeito certo</h2>
            <p>Hoje eu trato <code>.aab</code>, assinatura e keystore como parte critica da saude do app. Se isso ficar baguncado, a dor vem depois, especialmente quando chega a hora de publicar novas versoes.</p>
            <ol>
                <li>Atualize versao e <code>versionCode</code>.</li>
                <li>Gere o bundle assinado no Android Studio.</li>
                <li>Guarde keystore e chave de upload em local seguro.</li>
                <li>Confirme se ambiente, endpoints e flags de producao estao corretos.</li>
            </ol>
            <h2>O que costuma dar problema</h2>
            <ul>
                <li>Formulario de seguranca de dados preenchido sem cuidado.</li>
                <li>Build assinado de forma improvisada.</li>
                <li>Release criada sem revisar strings, imagens e metadados.</li>
                <li>Falta de teste minimo em um build realmente proximo do ambiente final.</li>
            </ul>
            <blockquote>Publicar bem e pensar no app depois da publicacao. O deploy certo nao termina quando a release entra no ar, e quando voce consegue manter e evoluir sem caos.</blockquote>
            <h2>Referencia oficial</h2>
            <p>Para a parte formal de assinatura e bundle, vale consultar a documentacao oficial: <a href="https://developer.android.com/studio/publish/app-signing?hl=pt-br" target="_blank" rel="noreferrer">Android Developers - Assinar seu aplicativo</a>.</p>
        """,
    },
    {
        "file": "blog-8.html",
        "category": "Unity",
        "date": "26/05/2026",
        "read_time": "7 min",
        "card_title": "Flappy Bird em Unity",
        "title": "Como eu pensaria um Flappy Bird em Unity para estudar bem",
        "description": "Um caminho pratico para construir Flappy Bird em Unity com foco em gameplay, iteracao e aprendizado tecnico.",
        "cover": "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=stylized%202d%20side%20scrolling%20bird%20game%20development%20scene%2C%20indie%20mobile%20game%20tutorial%20cover%2C%20colorful%20sky%2C%20pipes%20obstacles%2C%20playful%20polished%20art%2C%20professional%20composition%2C%20no%20text&image_size=landscape_16_9",
        "card_cover": "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=stylized%202d%20side%20scrolling%20bird%20game%20development%20scene%2C%20indie%20mobile%20game%20tutorial%20cover%2C%20colorful%20sky%2C%20pipes%20obstacles%2C%20playful%20polished%20art%2C%20professional%20composition%2C%20no%20text&image_size=landscape_16_9",
        "lead": "Projetos pequenos como Flappy Bird sao otimos porque concentram muita coisa importante em pouco escopo: fisica, input, spawn, colisao, pontuacao, feedback e reinicio de loop. E exatamente por isso eu gosto deles para estudo.",
        "summary": "Um roteiro de estudo em Unity focado em terminar um jogo simples, polido e util para aprendizado.",
        "content": """
            <h2>Por que eu gosto desse tipo de projeto</h2>
            <p>Como tenho interesse forte em desenvolvimento de jogos e ja passei por contextos ligados a Unity, eu vejo clones pequenos como laboratorios de aprendizado. Eles ajudam a fechar ciclo: planejar, montar cena, ajustar sensacao, polir e concluir.</p>
            <h2>O minimo que eu montaria primeiro</h2>
            <ul>
                <li>Um passaro com <code>Rigidbody2D</code> e <code>Collider2D</code>.</li>
                <li>Um prefab de tubos com espaco central para passagem.</li>
                <li>Um spawner simples com intervalo fixo.</li>
                <li>UI com score atual e tela de game over.</li>
            </ul>
            <h2>A mecanica principal</h2>
            <p>O ponto mais importante e a sensacao do pulo. Eu gosto de resetar a velocidade vertical antes de aplicar o impulso, porque isso deixa a resposta mais consistente.</p>
            <pre><code>if (Input.GetMouseButtonDown(0)) {
    rb.velocity = Vector2.up * jumpForce;
}</code></pre>
            <h2>O que transforma estudo em projeto de verdade</h2>
            <ul>
                <li>Ajuste fino de velocidade, gravidade e abertura dos obstaculos.</li>
                <li>Animacao simples para dar vida ao personagem.</li>
                <li>Efeitos sonoros para ponto, pulo e colisao.</li>
                <li>Tela inicial, restart e melhor score.</li>
            </ul>
            <h2>O valor tecnico por tras de um jogo simples</h2>
            <p>Esse tipo de projeto parece pequeno, mas ensina muito sobre ritmo de interacao, dificuldade, feedback e polimento. E um bom exemplo de como jogos ajudam a desenvolver sensibilidade para software interativo no geral.</p>
            <blockquote>Eu gosto de projetos assim porque eles treinam algo essencial: terminar, observar o resultado, ajustar e aprender com o que foi construido.</blockquote>
        """,
    },
    {
        "file": "blog-9.html",
        "category": "Observabilidade",
        "date": "26/05/2026",
        "read_time": "8 min",
        "card_title": "Logs com GCP e Dynatrace",
        "title": "Como eu pensaria observabilidade com GCP Logging e Dynatrace",
        "description": "Um tutorial pratico sobre observabilidade com foco em logs, sinais importantes e leitura de incidente em producao.",
        "cover": "../images/works/work-01.jpg",
        "card_cover": "images/works/work-01.jpg",
        "lead": "Depois de trabalhar com monitoramento e operacao em ambientes reais, eu passei a ver observabilidade como uma ferramenta de clareza. O objetivo nao e ter mil dashboards, e descobrir rapido o que esta quebrando, onde e por que.",
        "summary": "Um guia direto para pensar logs, alertas e investigacao usando GCP Logging e Dynatrace.",
        "content": """
            <h2>De onde vem essa visao</h2>
            <p>Na minha experiencia com times de plataforma e DevSecOps, eu lidei com GCP Logging, Dynatrace, Jenkins, Docker, Kubernetes e analise de comportamento em producao. Isso me ensinou que observabilidade boa precisa ser objetiva.</p>
            <h2>O que eu priorizo primeiro</h2>
            <ul>
                <li>Logs com contexto: servico, ambiente, request id e severidade.</li>
                <li>Separacao entre erro de aplicacao, erro de integracao e ruido tecnico.</li>
                <li>Dashboards que respondem perguntas reais, nao so mostram numero.</li>
                <li>Alertas com limiar razoavel e dono claro.</li>
            </ul>
            <h2>Como eu organizaria os logs</h2>
            <ol>
                <li>Padronize formato de log antes de qualquer ferramenta.</li>
                <li>Garanta campos que ajudem a filtrar por servico, rota e incidente.</li>
                <li>Use GCP Logging para busca rapida e correlação inicial.</li>
                <li>Use Dynatrace para entender impacto, dependencias e degradacao.</li>
            </ol>
            <h2>O erro comum</h2>
            <p>Muita gente manda tudo para a plataforma de monitoramento e espera magia. Sem padrao de log, sem contexto e sem alertas bem pensados, a ferramenta so vira um deposito caro de ruido.</p>
            <blockquote>Observabilidade nao e acumular telemetria. E reduzir tempo de duvida quando a producao comeca a se comportar de forma estranha.</blockquote>
            <h2>Um bom ponto de partida</h2>
            <p>Se eu estivesse montando isso do zero, comecaria por um servico critico, uma trilha clara de log e dois ou tres alertas que representam dor real do negocio.</p>
        """,
    },
    {
        "file": "blog-10.html",
        "category": "Python",
        "date": "26/05/2026",
        "read_time": "7 min",
        "card_title": "API Flask organizada",
        "title": "Como eu estruturaria uma API Flask pensando em produto real",
        "description": "Uma forma pratica de montar API Flask com organizacao, clareza e caminho para crescer sem virar bagunca.",
        "cover": "../images/works/work-03.png",
        "card_cover": "images/works/work-03.png",
        "lead": "Flask parece simples no inicio, e isso e exatamente o que pode virar problema depois. Quando voce usa a stack em produto real, aprende rapido que estrutura, convencao e separacao de responsabilidade importam muito.",
        "summary": "Uma base pratica para iniciar Flask com organizacao suficiente para projeto real.",
        "content": """
            <h2>Por que esse tema faz sentido para mim</h2>
            <p>Hoje eu trabalho com Python Flask em contexto profissional e ja usei essa stack em projetos onde manutencao, clareza e evolucao contam mais do que simplesmente fazer a rota responder.</p>
            <h2>O que eu separaria desde cedo</h2>
            <ul>
                <li>Camada de rotas para entrada e saida HTTP.</li>
                <li>Camada de servicos para regra de negocio.</li>
                <li>Camada de repositorio para acesso a banco.</li>
                <li>Configuracao por ambiente sem valores espalhados.</li>
                <li>Tratamento de erro padronizado.</li>
            </ul>
            <h2>Como eu evitaria o caos</h2>
            <p>O erro mais comum em Flask e deixar controller virar regra de negocio, query, validacao e formatacao tudo junto. Funciona no inicio e vira gargalo rapido quando o produto cresce.</p>
            <h2>Checklist minimo para eu considerar saudavel</h2>
            <ol>
                <li>Blueprints por dominio.</li>
                <li>Config centralizada por ambiente.</li>
                <li>Validacao de payload antes da regra.</li>
                <li>Logs minimamente padronizados.</li>
                <li>Testes de fluxo critico.</li>
            </ol>
            <blockquote>Flask fica muito bom quando voce resiste a tentacao de deixar tudo simples demais por tempo demais.</blockquote>
            <h2>Onde eu usaria essa abordagem</h2>
            <p>Ela encaixa bem em APIs internas, produtos menores em crescimento e servicos que precisam manter legibilidade sem obrigar o time a entrar em uma arquitetura pesada cedo demais.</p>
        """,
    },
    {
        "file": "blog-11.html",
        "category": "DevOps",
        "date": "26/05/2026",
        "read_time": "9 min",
        "card_title": "CI/CD com Jenkins",
        "title": "Como eu penso um pipeline CI/CD com Jenkins, Docker e Kubernetes",
        "description": "Uma visao pratica sobre pipeline de entrega continua que conecta build, testes, imagem, deploy e rollback com menos friccao.",
        "cover": "../images/portfolio-content/DevOpsStudy/devops.webp",
        "card_cover": "images/portfolio-content/DevOpsStudy/devops.webp",
        "lead": "Quando pipeline e mal pensado, o time perde confianca na entrega. Quando e bem pensado, ele vira parte natural do trabalho. Foi convivendo com Jenkins, Docker, Kubernetes e ambientes reais que eu formei essa leitura mais pragmatica.",
        "summary": "Um roteiro pratico para pensar pipeline CI/CD de forma confiavel e util para o time.",
        "content": """
            <h2>Meu ponto de partida</h2>
            <p>Eu gosto de pipeline que tenha poucas etapas, mas cada uma com papel claro: validar, empacotar, publicar e implantar. Complexidade sem motivo costuma enfraquecer a confianca do time.</p>
            <h2>Etapas que eu considero basicas</h2>
            <ol>
                <li>Instalar dependencias e preparar ambiente.</li>
                <li>Rodar lint e testes relevantes.</li>
                <li>Gerar imagem Docker versionada.</li>
                <li>Publicar a imagem em registry.</li>
                <li>Atualizar deploy no Kubernetes com rastreabilidade.</li>
            </ol>
            <h2>O que eu evitaria</h2>
            <ul>
                <li>Pipeline com dezenas de etapas sem ganho real.</li>
                <li>Deploy sem versionamento claro de imagem.</li>
                <li>Segredo espalhado em job ou script solto.</li>
                <li>Rollback improvisado.</li>
            </ul>
            <h2>Por que isso conversa com minha experiencia</h2>
            <p>Minha experiencia com plataforma, DevSecOps e ambiente cloud me ensinou que o pipeline precisa ser uma extensao da rotina de engenharia. Se ele gera medo, ele esta mal desenhado.</p>
            <blockquote>O melhor pipeline nao e o mais impressionante no diagrama. E o que o time usa sem receio para entregar mudanca com consistencia.</blockquote>
            <h2>Minha regra pratica</h2>
            <p>Se eu nao consigo explicar em poucos minutos como o pipeline sobe, valida e volta atras, ele provavelmente esta complicado demais.</p>
        """,
    },
    {
        "file": "blog-12.html",
        "category": "Web3",
        "date": "26/05/2026",
        "read_time": "8 min",
        "card_title": "NestJS + Solidity",
        "title": "Como eu estruturaria um backend web3 com NestJS e Solidity",
        "description": "Um tutorial conceitual sobre separar API, integracao blockchain e regras de negocio em um backend web3 mais legivel.",
        "cover": "../images/projects/kypto.png",
        "card_cover": "images/projects/kypto.png",
        "lead": "Web3 costuma ficar confuso rapido quando smart contract, API, persistencia e regra de negocio se misturam. Como eu ja trabalhei com NestJS, Solidity e projetos desse tipo, minha tendencia e separar muito bem as responsabilidades.",
        "summary": "Uma forma pratica de pensar backend web3 sem misturar tudo em uma unica camada.",
        "content": """
            <h2>O erro que eu mais evitaria</h2>
            <p>Em muito projeto web3, a integracao com blockchain invade tudo. A API passa a conhecer detalhes demais do contrato, e a regra de negocio fica presa a adaptadores especificos. Isso dificulta teste, evolucao e leitura.</p>
            <h2>Como eu separaria</h2>
            <ul>
                <li>Controllers e DTOs para entrada e saida HTTP.</li>
                <li>Services para regra de negocio.</li>
                <li>Camada de integracao blockchain isolada.</li>
                <li>Persistencia off-chain separada da logica do contrato.</li>
                <li>Mapeamento claro entre evento on-chain e dado interno.</li>
            </ul>
            <h2>Onde NestJS ajuda</h2>
            <p>NestJS me agrada nesse contexto porque organizacao, modulos, providers e injecao de dependencia ajudam a manter o sistema legivel mesmo quando a integracao com contratos cresce.</p>
            <h2>Onde Solidity pede atencao</h2>
            <ul>
                <li>Interface pequena e bem definida.</li>
                <li>Eventos pensados para observacao e sincronizacao.</li>
                <li>Validacao e seguranca desde o desenho inicial.</li>
                <li>Separacao entre o que deve ficar on-chain e off-chain.</li>
            </ul>
            <blockquote>Projeto web3 saudavel e aquele em que a blockchain e parte importante da arquitetura, mas nao sequestra toda a engenharia do produto.</blockquote>
            <h2>Minha prioridade em projetos assim</h2>
            <p>Eu tentaria garantir clareza, previsibilidade de integracao e uma boa camada de observacao. Em web3, entender o que aconteceu e tao importante quanto disparar a transacao.</p>
        """,
    },
]


def render_related_cards(current_file: str) -> str:
    items = [article for article in articles if article["file"] != current_file][:2]
    return "".join(
        f'<article class="related-card"><h3>{item["card_title"]}</h3><p>{item["summary"]}</p><a class="back-link" href="{item["file"]}">Ler artigo</a></article>'
        for item in items
    )


def render_more_articles(current_file: str) -> str:
    return "".join(
        f'<li><a href="{item["file"]}">{item["card_title"]}</a></li>'
        for item in articles
        if item["file"] != current_file
    )


def render_article(article: dict) -> str:
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article["title"]} | Harold Illert</title>
    <meta name="description" content="{article["description"]}">
    <link rel="shortcut icon" href="../favicon.ico" type="image/x-icon">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../icon-fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/article-page.css">
</head>
<body class="article-page">
    <header class="site-header" id="topo">
        <div class="container header-inner">
            <a class="brand" href="../index.html">Harold Illert</a>
            <button class="menu-toggle" type="button" aria-label="Abrir menu" aria-expanded="false">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <nav class="subpage-nav">
                <a href="../index.html#sobre">Sobre</a>
                <a href="../index.html#experiencia">Experiencia</a>
                <a href="../index.html#projetos">Projetos</a>
                <a href="../index.html#artigos" class="active">Artigos</a>
                <a href="../index.html#contato">Contato</a>
            </nav>
        </div>
    </header>

    <main class="article-main">
        <div class="container article-shell">
            <section class="article-grid">
                <article class="article-hero">
                    <img class="article-cover" src="{article["cover"]}" alt="Capa do artigo {article["title"]}">
                    <div class="article-body-wrap">
                        <div class="article-meta">
                            <span class="meta-pill">{article["category"]}</span>
                            <span class="meta-pill">{article["date"]}</span>
                            <span class="meta-pill">{article["read_time"]}</span>
                        </div>
                        <h1 class="article-title">{article["title"]}</h1>
                        <p class="article-lead">{article["lead"]}</p>
                    </div>
                </article>

                <article class="article-card">
                    <div class="article-prose">
                        {article["content"].strip()}
                    </div>
                </article>

                <article class="note-card">
                    <h3>Resumo rapido</h3>
                    <p>{article["summary"]}</p>
                    <a class="back-link" href="../index.html#artigos"><i class="fa fa-arrow-left" aria-hidden="true"></i> Voltar para os artigos</a>
                </article>

                <div class="related-grid">
                    {render_related_cards(article["file"])}
                </div>
            </section>

            <aside class="aside-stack">
                <section class="aside-card">
                    <div class="author-mini">
                        <img src="../images/profile.jpg" alt="Foto de Harold Illert">
                        <div>
                            <strong>Harold Illert</strong>
                            <p>Engenheiro de software com foco em full-stack, cloud, web3 e games.</p>
                        </div>
                    </div>
                    <a class="btn btn-primary" href="../harold%20illert.pdf" target="_blank" rel="noreferrer">Abrir curriculo</a>
                </section>
                <section class="aside-card">
                    <h3>Mais artigos</h3>
                    <ul class="aside-list">
                        {render_more_articles(article["file"])}
                    </ul>
                </section>
                <section class="aside-card">
                    <h3>Links diretos</h3>
                    <ul class="aside-list">
                        <li><a href="https://github.com/harryninja" target="_blank" rel="noreferrer">GitHub</a></li>
                        <li><a href="https://www.linkedin.com/in/harold-illert/" target="_blank" rel="noreferrer">LinkedIn</a></li>
                        <li><a href="https://harryninja.itch.io/" target="_blank" rel="noreferrer">Itch.io</a></li>
                        <li><a href="https://api.whatsapp.com/send?phone=5581988752949" target="_blank" rel="noreferrer">WhatsApp</a></li>
                    </ul>
                </section>
            </aside>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-inner">
            <p>(c) <span id="currentYear"></span> Harold Illert. Conteudo publicado no portfolio.</p>
        </div>
    </footer>

    <script src="../js/main.js"></script>
</body>
</html>
"""


def render_home_articles() -> str:
    cards = []
    for article in articles:
        cards.append(
            f"""                    <a class="article-card glass-card" href="blog-posts/{article["file"]}" target="_blank" rel="noreferrer">
                        <img src="{article["card_cover"]}" alt="Thumbnail do artigo {article["card_title"]}">
                        <div>
                            <span>{article["category"]}</span>
                            <h3>{article["card_title"]}</h3>
                        </div>
                    </a>"""
        )
    return """<section class="section section-soft" id="artigos">
            <div class="container">
                <div class="section-heading compact">
                    <span class="eyebrow">Conteudo</span>
                    <h2>Artigos e tutoriais publicados</h2>
                    <p>Ampliei a secao com tutoriais conectados a minha vivencia em full-stack, cloud, mobile, observabilidade, DevOps, web3 e games.</p>
                </div>
                <div class="article-grid">
""" + "\n".join(cards) + """
                </div>
            </div>
        </section>"""


for article in articles:
    (blog_dir / article["file"]).write_text(render_article(article), encoding="utf-8")

index_text = index_path.read_text(encoding="utf-8")
section_start = index_text.index('<section class="section section-soft" id="artigos">')
section_end = index_text.index("</section>", section_start) + len("</section>")
index_text = index_text[:section_start] + render_home_articles() + index_text[section_end:]
index_path.write_text(index_text, encoding="utf-8")
