<script setup>
    const { data: LivroEnc} = await useFetch(`https://somativaandrelivraria-production.up.railway.app/api/auth/livros/`);
</script>

<template>
    <main class="livros-tela flex-center">
        <h2 class="mt-4 mb-4">📚 Acervo de Livros 📚</h2>
        <div class="lib">
            <div v-for="b in LivroEnc" :key="b.id">
                <LivroItem :index="b.id"/>
            </div>
        </div>
    </main>
</template>

<style scoped lang="scss">

    .livros-tela{
        margin: 0;
        width: 100vw;
        min-height: calc(100vh - 80px);
        background-color: red;
        background-image: url("background.jpg");
        background-repeat: repeat;
        background-size: cover;

        h2{
            color: black;
        }
    }

    .flex-center{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
    }

    .lib{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
</style>