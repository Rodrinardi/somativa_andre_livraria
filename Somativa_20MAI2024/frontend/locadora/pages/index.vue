<script setup lang="ts">
import { reactive, ref } from 'vue';
const { signIn } = useAuth();
const credenciais = reactive({
    email: '',
    password: ''
});
const mensagemErro = ref('');

const fazerLogin = () => {
    console.log("login: ", credenciais);
    signIn(credenciais, { redirect: false })
        .then(() => {
             console.log("logado com sucesso....");
             navigateTo('/home');
         })
        .catch((error) => {
            console.error("error: ", error);
            mensagemErro.value = 'usuário ou senha inválidos';
            setTimeout(() => {
                mensagemErro.value = '';
                credenciais.email = '';
                credenciais.password = '';
            }, 3000);
        })
}


const painel = ref();

const toggle = (event: any) => {
    painel.value.toggle(event);
}
</script>

<template>
    <main class="login-main flex align-items-center justify-content-center">
        <div class="chatbot">
            <Button type="button" icon="pi pi-comment" label="Chatbot" @click="toggle" />
            <OverlayPanel ref="painel">
                <iframe allow="microphone;" width="350" height="430"
                    src="https://console.dialogflow.com/api-client/demo/embedded/6cea1cd9-a872-4f2b-97cc-ec36e8402522">
                </iframe>
            </OverlayPanel>
        </div>
        <section class="login-container flex flex-column align-items-center justify-content-center">
            <h4 class="row-login">Locação de livros Seraiva</h4>
            <div class="row-login">
                <FloatLabel>
                    <InputText v-model="credenciais.email" type="email" id="email-input" class="input-text" />
                    <label for="email-input">Email</label>
                </FloatLabel>
            </div>
            <div class="row-login">
                <FloatLabel>
                    <InputText v-model="credenciais.password" type="password" id="password-input" class="input-text" />
                    <label for="password-input">Senha</label>
                </FloatLabel>
            </div>
            <div class="row-login" v-if="mensagemErro !== ''">
                <p id="erro">{{ mensagemErro }}</p>
            </div>
            <div class="row-login">
                <Button @click="fazerLogin" label="Entrar" id="login-button"></Button>
            </div>
        </section>
    </main>
</template>


<style scoped lang="scss">
.login-main {
    width: 100vw;
    height: 100vh;
    background-image: url('background.jpg');
    background-repeat: repeat;
    background-size: cover;

    .login-container {
        width: 30vw;
        height: 70vh;
        background-color: white;

        .row-login {
            margin: 1rem 0 1rem 0;

            .input-text {
                height: 2.5rem;
                width: 250px;
            }

            #login-button {
                width: 250px;
                height: 30px;
            }

            #erro {
                color: tomato;
                font-size: 0.8rem;
            }
        }
    }
}
.chatbot{
    position: fixed;
    bottom: 0;
    right: 0;
    margin: 1rem
}
</style>