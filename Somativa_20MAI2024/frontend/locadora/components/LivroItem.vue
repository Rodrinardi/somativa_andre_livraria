<script setup>
    
    const prop = defineProps({
        index: {type: String}
    })

    const { data: LivroEnc} = await useFetch(`somativaandrelivraria-production.up.railway.app/api/auth/livros/${prop.index}`);
    
</script>

<template>
    <section class="item flex-center">
        <div class="imagem-livro">
            <nuxt-link :to="`/detalheLivro/${LivroEnc.id}`">
                <img :src="LivroEnc.fotoFK.url"/>
            </nuxt-link>
        </div>
        <div>
            <h4 class="nome-livro">{{ LivroEnc.titulo }}</h4>
        </div>
        <div class="flex flex-row">
            <span class="texto-valor">Valor: R${{ LivroEnc.valor }}</span>
        </div>
        <div class="m1-2">
                <label class="quantidade"> Qtd. Disponível: </label>
                <span class="quantidade">{{ LivroEnc.quantidade }}</span>
        </div>
        <Button class="botao-emp" v-if="LivroEnc.quantidade >= 1">Emprestar</Button>
        <Button class="botao-indisp" v-if="LivroEnc.quantidade <= 0">Indisponível</Button>
    </section>
</template>

<style scoped lang="scss">

    .flex-center{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .item{
        width: 300px;
        max-width: 300px;
        height: 400px;
        max-height: 400px;
        background-color: grey;
        border-radius: 0.5rem;
        margin: 1.5rem;
        transition: 0.5s;

        &:hover{
            transform: scale(1.1);
        }


        .imagem-livro{
            width: fit-content;
            height: fit-content;

            img{
                width: 136px;
                height: 200px;
            }
        }

        .nome-livro{
            margin: 0.5rem;
            color: black;
        }

        .botao-emp{
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
                background-color: green;
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

        .texto-valor{
            color: black;
        }

        .quantidade{
            color: black;
        }
    }
</style>