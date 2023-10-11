<template>
    <div>
        <div class="mb-1" style="display: flex;justify-content: space-between; align-items: center;">
            <div>
                <input class="input-group input-group-sm" style="width: unset !important;display: unset;"
                    v-model="searchText" placeholder="Search by Author" />
                <button class="btn btn-outline-secondary btn-sm" @click="filteredAuthors"
                    style="transform: translateY(-2px);">
                    <span>
                        <svg style="fill: white;" xmlns="http://www.w3.org/2000/svg" height="18" viewBox="0 -960 960 960"
                            width="18">
                            <path
                                d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z" />
                        </svg>
                    </span>
                </button>
            </div>
            <div>
                <button class="btn btn-outline-secondary btn-sm" style="transform: translateY(-2px);" @click="addAuthor">Add
                    Author</button>
            </div>
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Author</th>
                    <th scope="col" style="text-align: center;">Number of Books</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(author, index) in displayed_authors">
                    <th scope="row">{{ author.id }}</th>
                    <td>{{ author.author }}</td>
                    <td style="text-align: center;">{{ author.books.length }}</td>
                    <td>
                        <div class="btn-group" role="group" aria-label="actionss" style="transform: translateY(-1px);">
                            <button type="button" class="btn btn-outline-secondary btn-sm" @click="updateAuthor(author.id)">Update</button>
                            <button type="button" class="btn btn-outline-secondary btn-sm" @click="removeAuthor(author.id)">Remove</button>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- PAGINATION START -->
        <div class="pagination display-flex justify-content-center">
            <ul class="pagination pagination-sm">
                <li class="page-item" :class="{ 'disabled': currentPage === 1 }">
                    <a class="page-link" @click="goToPage(currentPage - 1)" href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
                <li class="page-item" v-for="page in totalPages" :key="page" :class="{ 'active': currentPage === page }">
                    <a class="page-link" @click="goToPage(page)" href="#">{{ page }}</a>
                </li>
                <li class="page-item" :class="{ 'disabled': currentPage === totalPages }">
                    <a class="page-link" @click="goToPage(currentPage + 1)" href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            </ul>
        </div>
        <!-- PAGINATION END -->
        <!-- MODAL > -->
        <b-modal v-model="modalShow" title="Author" @ok="submitAuthor">
            <b-form-group>
                <b-form-input v-if="actionType=='add'" v-model="authorName" placeholder="Author"></b-form-input>
                <b-form-input v-if="actionType=='update'" v-model="authorName" placeholder="Author"></b-form-input>
                <p v-if="actionType=='delete'">Are you sure want to remove this Author?</p>
            </b-form-group>
        </b-modal>
    </div>
</template>

<script lang="ts">

export default {
    data() {
        return {
            url: "http://127.0.0.1:8000/api/author",
            authors: [] as { id: number, author: string, books: any }[],
            displayed_authors: [] as { id: number, author: string, books: any }[],
            filtered_authors: [] as { id: number, author: string, books: any }[],
            searchText: "",
            currentPage: 1,
            itemsPerPage: 5,
            modalShow: false,
            authorName: "",
            authorId: 0,
            actionType: ""
        }

    },
    computed: {
        totalPages() {
            if (this.searchText && this.filtered_authors.length > 0) {
                return Math.ceil(this.filtered_authors.length / this.itemsPerPage);
            } else {
                return Math.ceil(this.authors.length / this.itemsPerPage);
            }
        }
    },
    methods: {
        filteredAuthors() {
            if (!this.searchText) {
                this.displayed_authors = this.authors.slice(0, this.itemsPerPage);
                this.filtered_authors = []
            } else {
                const searchTextLowerCase = this.searchText.toLowerCase();
                let authors = this.authors.filter(author => {
                    return author.author.toLowerCase().includes(searchTextLowerCase);
                });
                this.filtered_authors = authors;
                this.displayed_authors = this.filtered_authors.slice(0, this.itemsPerPage)
            }
        },
        goToPage(pageNumber: number) {
            if (pageNumber >= 1 && pageNumber <= this.totalPages) {
                this.currentPage = pageNumber;
                const startIndex = (pageNumber - 1) * this.itemsPerPage;
                const endIndex = startIndex + this.itemsPerPage;
                if (this.filtered_authors.length > 0) {
                    this.displayed_authors = this.filtered_authors.slice(startIndex, endIndex);
                } else {
                    this.displayed_authors = this.authors.slice(startIndex, endIndex);
                }
            }
        },
        showModal() {
            this.modalShow = true;
        },
        hideModal() {
            this.modalShow = false;
        },
        async fetchAuthors() {
            const response = await this.$axios.get(this.url, {
                headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
            }).catch((err) => {
                console.log(err);
            });
            if (!response || response.status != 200) {
                console.error(response)
            } else {
                this.authors = response.data
                this.displayed_authors = this.authors.slice(0, this.itemsPerPage);
            }
        },
        async submitAuthor() {
            let response;
            if (this.actionType == "add") {
                response = await this.$axios.post(this.url,
                    {
                        author: this.authorName,
                        books: []
                    },
                    {
                        headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
                    }
                ).catch(err => console.log(err))
            } else if (this.actionType == "delete") {
                response = await this.$axios.delete(this.url + '/' + this.authorId,
                    {
                        headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
                    }
                ).catch(err => console.log(err))
            } else if (this.actionType == "update") {
                response = await this.$axios.put(this.url+ '/' + this.authorId,
                    {
                        author: this.authorName,
                    },
                    {
                        headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
                    }
                ).catch(err => console.log(err))
            }
            if (response && response.status == 200) {
                this.fetchAuthors();
            }
            this.authorName = "";
            this.authorId = 0;
        },
        addAuthor() {
            this.actionType = "add";
            this.showModal();
        },
        removeAuthor(id: any) {
            this.authorId = id;
            this.actionType = "delete";
            this.showModal()
        },
        updateAuthor(id: any) {
            let author = this.authors.find(x => x.id == id);
            this.authorId = author?.id || 0;
            this.authorName = author?.author || "";
            this.actionType = "update";
            this.showModal()
        }
    },
    async fetch() {
        await this.fetchAuthors();
    }
}
</script>

<style scoped>
.table {
    color: white;
    font-weight: 200;
}
</style>