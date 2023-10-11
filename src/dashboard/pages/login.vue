<template>
    <div>
        <div class="custom-container">
            <div class="sign-in-form">
                <div class="card">
                    <form @submit.prevent="login">
                        <img class="mb-4" src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg" alt=""
                            width="72" height="57">
                        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

                        <div class="form-floating">
                            <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com"
                                v-model="username">
                            <label for="floatingInput">Email address</label>
                        </div>
                        <div class="form-floating">
                            <input type="password" class="form-control" id="floatingPassword" placeholder="Password"
                                v-model="password">
                            <label for="floatingPassword">Password</label>
                        </div>

                        <button class="btn btn-primary w-100 py-2 mt-3" @click="login">Sign in</button>
                        <p class="text-body-secondary mt-1">© 2017-2023</p>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import useRouter from 'vue-router';
import useRoute from 'vue-router';
import axios from 'axios';

export default {
    data() {
        return {
            username: "",
            password: "",
            url: "http://127.0.0.1:8000/api/auth/login",
        }
        
    },
    methods: {
        async login() {
            const response = await this.$axios.post(this.url, {
                username: this.username,
                password: this.password
            });
            if (response.status == 200) {
                // go to home
                localStorage.setItem("fast_token", response.data.token)
                this.$router.push('/')
            } else {
                // error
                console.error(response)
            }
        }
    }

}

</script>

<style scoped>
.custom-container {
    width: 100%;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-image: url("assets/images/endless-constellation.png");
}

.sign-in-form {
    width: 50%;
    height: 50%;
    max-width: 500px;
    max-height: 600px;
}

.card {
    padding: 20px;
}

.card {
    background-color: rgba(255, 255, 255, 0.496);
}
</style>