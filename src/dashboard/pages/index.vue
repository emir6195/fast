<template>
    <div class="main-container">
        <Navbar />
        <div class="container">
            <div class="row">
                <Jumbo />
            </div>
            <div class="row">
                <div v-for="(item, index) in cards" class="col-sm-12 col-md-4">
                    <MainCard :title="item.title" :subtitle="item.subtitle" :link="item.link"
                        :button_text="item.button_text" />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">

import MainCard from '~/components/MainCard.vue';

export default {
    data() {
        return {
            url: "http://127.0.0.1:8000/api/auth/validate",
            cards: [
                {
                    title: "Discover Inspiring Authors",
                    subtitle: "Explore the diverse world of literary genius. Dive into the profiles of renowned authors who have shaped the literary landscape. From classic novelists to contemporary wordsmiths, uncover their life stories, inspirations, and their most celebrated works. Get ready to embark on a journey through the minds of literary legends.",
                    link: "/authors",
                    button_text: "Explore Authors"
                },
                {
                    title: "Explore Fascinating Books",
                    subtitle: "Immerse yourself in the enchanting world of books. Browse through an extensive collection of literary masterpieces, from timeless classics to contemporary bestsellers. Discover a treasure trove of genres, themes, and stories that will take you on unforgettable journeys. Whether you're an avid reader or just starting your reading adventure.",
                    link: "/books",
                    button_text: "Discover Books"
                }
            ]
        };
    },
    methods: {
        unauth() {
            localStorage.removeItem("fast_token");
            this.$router.push("/login");
        },
        logout() {
            this.unauth();
        }
    },
    async fetch() {
        const response = await this.$axios.get(this.url, {
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("fast_token")
            }
        }).catch((err) => {
            console.log(err);
            this.unauth();
        });
        if (!response || response.status != 200) {
            this.unauth();
        }
    },
    components: { MainCard }
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