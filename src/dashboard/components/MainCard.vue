<template>
    <div>
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">{{ title }}</h5>
                <h6 class="card-subtitle mb-2">{{ subtitle }}</h6>
                <NuxtLink :to="link" class="card-link">{{ button_text }}</NuxtLink>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: "",
        subtitle: "",
        link: "",
        button_text: "",
    }
}
</script>

<style scoped>

.card {
    background-color: rgba(255, 255, 255, 0.496);
}

.card-title {
    color: white;
}
.card-subtitle {
    color: white;
    font-weight: 100;
}

.card-link {
    color: rgb(47, 45, 45);
    text-decoration: underline;
}

</style>