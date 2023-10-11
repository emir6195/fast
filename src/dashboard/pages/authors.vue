<template>
    <div>
        <div class="main-container">
            <Navbar />
            <div class="container">
                <div class="row">
                    <MainDesc :description="description" />
                </div>
                <div class="row justify-content-center">
                    <AuthorTable />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
// import MainDesc from '../components/MainDesc.vue';

export default {
    data() {
        return {
            url: "http://127.0.0.1:8000/api/auth/validate",
            description: "Welcome to the heart of literary brilliance! On this page, we celebrate the creative minds behind some of the most remarkable books ever written. Our curated collection of authors spans across genres, eras, and cultures, bringing together the essence of storytelling from around the world."
        }

    },
    components: {
        // MainDesc
    },
    methods: {
        unauth() {
            localStorage.removeItem("fast_token")
            this.$router.push("/login")
        },
    },
    async fetch() {
        const response = await this.$axios.get(this.url, {
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("fast_token")
            }
        }).catch((err) => {
            console.log(err);
            this.unauth()
        });
        if (!response || response.status != 200) {
            this.unauth()
        }
    }
}
</script>

<style scoped>
.main-container {
    min-height: 100vh;
    background-image: url("assets/images/endless-constellation.png");
}

.container {
    padding: 20px;
}
</style>