<template>
    <nav class="navbar bg-body-tertiary bg-dark">
        <div class="container">
            <div class="left-side">
                <a class="navbar-brand">
                    <img src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap"
                        style="transform: translateY(-1px);" width="30" height="24">
                </a>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <NuxtLink class="nav-link" to="/">
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" height="21" viewBox="0 -960 960 960" width="21">
                                <path
                                    d="M240-200h120v-240h240v240h120v-360L480-740 240-560v360Zm-80 80v-480l320-240 320 240v480H520v-240h-80v240H160Zm320-350Z" />
                            </svg> -->
                            Home
                        </NuxtLink>
                    </li>
                    <li class="nav-item">
                        <NuxtLink class="nav-link" to="/authors">
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" height="21" viewBox="0 -960 960 960" width="21">
                                <path
                                    d="M280-600q-33 0-56.5-23.5T200-680q0-33 23.5-56.5T280-760q33 0 56.5 23.5T360-680q0 33-23.5 56.5T280-600ZM200-80q-17 0-28.5-11.5T160-120q-33 0-56.5-23.5T80-200v-240h120v-30q0-38 26-64t64-26q20 0 37 8t31 22l56 62q8 8 15.5 15t16.5 13h274v-326q0-14-10-24t-24-10q-6 0-11.5 2.5T664-790l-50 50q5 17 2 33.5T604-676L494-788q14-9 30-11.5t32 3.5l50-50q16-16 36.5-25t43.5-9q48 0 81 33t33 81v326h80v240q0 33-23.5 56.5T800-120q0 17-11.5 28.5T760-80H200Zm-40-120h640v-160H160v160Zm0 0h640-640Z" />
                            </svg> -->
                            Authors
                        </NuxtLink>
                    </li>
                    <li class="nav-item">
                        <NuxtLink class="nav-link" to="/books">
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" height="21" viewBox="0 -960 960 960" width="21">
                                <path
                                    d="M480-160q-48-38-104-59t-116-21q-42 0-82.5 11T100-198q-21 11-40.5-1T40-234v-482q0-11 5.5-21T62-752q46-24 96-36t102-12q58 0 113.5 15T480-740v484q51-32 107-48t113-16q36 0 70.5 6t69.5 18v-480q15 5 29.5 10.5T898-752q11 5 16.5 15t5.5 21v482q0 23-19.5 35t-40.5 1q-37-20-77.5-31T700-240q-60 0-116 21t-104 59Zm80-200v-380l200-200v400L560-360Zm-160 65v-396q-33-14-68.5-21.5T260-720q-37 0-72 7t-68 21v397q35-13 69.5-19t70.5-6q36 0 70.5 6t69.5 19Zm0 0v-396 396Z" />
                            </svg> -->
                            Books
                        </NuxtLink>
                    </li>
                </ul>
            </div>
            <div class="right-side">
                <ul class="navbar-nav">

                    <li class="nav-item">
                        <a class="nav-link logout" @click="logout">
                            <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 -960 960 960" width="20">
                                <path
                                    d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h280v80H200v560h280v80H200Zm440-160-55-58 102-102H360v-80h327L585-622l55-58 200 200-200 200Z" />
                            </svg>
                            Logout
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script lang="ts">
import useRouter from 'vue-router';
import useRoute from 'vue-router';
import axios from 'axios';

export default {
    methods: {
        unauth() {
            localStorage.removeItem("fast_token")
            this.$router.push("/login")
        },
        logout() {
            this.unauth()
        }
    },
}
</script>

<style scoped>
svg {
    fill: white;
    transform: translate(0px, -1.5px);
    margin-right: 3px;
}

.navbar-nav {
    flex-direction: row;
}

.nav-item {
    margin-right: 15px;
    font-weight: 200;
    margin-left: 5px;
}

.nav-item a {
    color: white;
}

.nav-item a:hover {
    color: rgb(197, 83, 197);
}

.left-side,
.right-side {
    display: flex;
}

.logout {
    cursor: pointer;
}

.bg-dark {
    background-color: #343a4078 !important;
}
</style>