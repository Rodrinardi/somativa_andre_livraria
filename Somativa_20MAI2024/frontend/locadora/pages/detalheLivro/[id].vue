<script setup>
    const route = useRoute();
    const {data: LivroEnc} = await useFetch(`http://127.0.0.1:8000/api/auth/livros/${route.params.id}`);
</script>

<template>
    <section class="tela-desc">
        <div class="info-livro">
            <div class="capa-livro">
                <img :src="LivroEnc.fotoFK.url" alt="Capa do Livro" width="500">
            </div>
            <br><br>
            <h1>Título: {{ LivroEnc.titulo }}</h1>
            <br>
            <h3>Quantidade Disponível: {{ LivroEnc.quantidade }}</h3>
            <br>
            <h3>Valor: R${{ LivroEnc.valor }}</h3>
            <br>
            <h3>Gênero: {{ LivroEnc.GeneroLivroFK.nome }}</h3>
            <br>
            <h3>Editora: {{ LivroEnc.editora}}</h3>
            <br>
            <h3>Publicação: {{ LivroEnc.publicacao }}</h3>

            <Button class="botao-emp" v-if="LivroEnc.quantidade >= 1">Emprestar</Button>
            <Button class="botao-indisp" v-if="LivroEnc.quantidade <= 0">Indisponível</Button>
        </div>
        <div class="livro-desc">
            <div class="painel-desc">
                <h1>Descrição:</h1>
                <br>
                <h3>{{ LivroEnc.descricao }}</h3>
            </div>
        </div>
    </section>
</template>

<style scoped lang="scss">

    .tela-desc{
        width: 100vw;
        height: 100vh;
        background-color: grey;
        display: flex;
        flex-direction: row;
    }

    .livro-desc{
        height: 100vh;
        width: 50vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
        
        .painel-desc{
            min-height: 100vh;
            max-height: 100vh;
            min-width: 45vw;
            max-width: 45vw;
            background-color: rgba(219, 219, 219, 0.771);
            padding: 15px;

            h1{
                color: black;
            }

            h3{
                color: black;
            }
        }
    }

    .info-livro{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 50vw;
        height: 100vh;
        background-color: rgba(219, 219, 219, 0.771);

        .botao-emp{
            margin-top: 30px;
            color: black;
            font-size: large;
            font-weight: bold;
            background-color: white;
            border-radius: 3px;
            border-width: 0;
            width: 75%;
            height: 10%;
            transition: 0.5s;

            &:hover{
                cursor: pointer;
                color: white;
                background-color: green;
                transform: scale(1.1);
            }

        }

        .botao-indisp{
            width: 80%;
            height: 2rem;
            margin: 1rem;
            color: black;
            font-weight: bold;
            background-color: white;
            border: 0;
            border-radius: 5px;
            transition: 0.5s;
            cursor: pointer;
            
            &:hover{
                color: white;
                font-weight: bold;
                background-color: red;
            }
        }

        .capa-livro{
            img{
                width: 339px;
                height: 500px;
                position: relative;
            }
        }

        h1{
            color: black;
        }

        h3{
            color: black;
        }
    }

</style>