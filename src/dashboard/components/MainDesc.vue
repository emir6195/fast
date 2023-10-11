<template>
    <div class="jumbotron">
        <p class="lead">{{ description }}</p>
    </div>
</template>

<script>
export default {
    props: {
        description: ""
    }
}

</script>

<style scoped>
.jumbotron {
    margin-bottom: 50px;
    background-color: transparent;
    padding: unset;
    padding: 0 15px;
}

h3,
p {
    color: white;
}

p {
    font-weight: 100 !important;
}
</style>