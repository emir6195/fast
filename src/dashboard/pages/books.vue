<template>
    <div>
        <div class="main-container">
            <Navbar />
            <div class="container">
                <div class="row">
                    <MainDesc :description="description" />
                </div>
                <div class="row justify-content-center">
                    <BookTable />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    data() {
        return {
            url: "http://127.0.0.1:8000/api/auth/validate",
            description: "Welcome to our treasure trove of literature! The 'Books' page is your gateway to a world of stories, adventures, and knowledge waiting to be explored. Whether you're an avid reader, a curious learner, or simply seeking your next literary journey, this is where the magic begins. From timeless classics that have stood the test of time to contemporary bestsellers that reflect the pulse of our modern world, our collection spans genres, cultures, and generations. Each book is a portal to a different world, a new perspective, and a chance to embark on unforgettable adventures. 📚"
        }

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
            },
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