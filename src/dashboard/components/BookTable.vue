<template>
    <div>
        <div class="mb-1" style="display: flex;justify-content: space-between; align-items: center;">
            <div>
                <input class="input-group input-group-sm" style="width: unset !important;display: unset;"
                    v-model="searchText" placeholder="Search by Book" />
                <button class="btn btn-outline-secondary btn-sm" @click="filteredBooks"
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
                <button class="btn btn-outline-secondary btn-sm" style="transform: translateY(-2px);" @click="addBook">Add
                    Book</button>
            </div>
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Book</th>
                    <th scope="col">Author</th>
                    <th scope="col" style="text-align: center;">Number of Pages</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(book, index) in displayed_books">
                    <th scope="row">{{ book.id }}</th>
                    <th scope="row">{{ book.name }}</th>
                    <td>{{ book.author?.author || '-' }}</td>
                    <td style="text-align: center;">{{ book.number_of_pages }}</td>
                    <td>
                        <div class="btn-group" role="group" aria-label="actionss" style="transform: translateY(-1px);">
                            <button type="button" class="btn btn-outline-secondary btn-sm"
                                @click="updateBook(book.id)">Update</button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"
                                @click="removeBook(book.id)">Remove</button>
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
        <b-modal v-model="modalShow" title="Book" @ok="submitBook">
            <b-form-group>
                <div v-if="actionType == 'add' || actionType == 'update'">
                    <label for="add-book-name" class="mt-2">Name</label>
                    <b-form-input id="add-book-name" v-model="bookName" placeholder="Book Name"></b-form-input>
                    <label for="add-book-author" class="mt-2">Author</label>
                    <b-form-select id="add-book-author" v-model="selectedAuthorId" :options="authors"
                        placeholder="Author"></b-form-select>
                    <label for="add-book-pages" class="mt-2">Number of Pages</label>
                    <b-form-input id="add-book-pages" v-model="number_of_pages" placeholder="Number of Pages"
                        @input="validateInput"></b-form-input>
                    <p v-if="validationError" class="text-danger">{{ validationError }}</p>
                </div>
                <div v-if="actionType == 'delete'">
                    <p>Are you sure want to remove this Book?</p>
                </div>
            </b-form-group>
        </b-modal>
    </div>
</template>

<script lang="ts">

export default {
    data() {
        return {
            url: "http://127.0.0.1:8000/api/book",
            author_url: "http://127.0.0.1:8000/api/author/no-join",
            books: [] as { id: number, author: { author: string, id: number }, name: string, author_id: number, number_of_pages: number }[],
            displayed_books: [] as { id: number, author: { author: string, id: number }, name: string, author_id: number, number_of_pages: number }[],
            filtered_books: [] as { id: number, author: { author: string, id: number }, name: string, author_id: number, number_of_pages: number }[],
            searchText: "",
            currentPage: 1,
            itemsPerPage: 5,
            modalShow: false,
            bookName: "",
            bookId: 0,
            actionType: "",
            number_of_pages: 0 as number,
            selectedAuthorId: null as any,
            authors: [] as { value: number, text: string }[],
            validationError: ""
        }

    },
    computed: {
        totalPages() {
            if (this.searchText && this.filtered_books.length > 0) {
                return Math.ceil(this.filtered_books.length / this.itemsPerPage);
            } else {
                return Math.ceil(this.books.length / this.itemsPerPage);
            }
        }
    },
    methods: {
        validateInput() {
            const input = this.number_of_pages;
            if (!Number.isInteger(input) || input <= 0) {
                this.validationError = 'Please enter a correct number.';
            } else {
                this.validationError = "";
            }
        },
        filteredBooks() {
            if (!this.searchText) {
                this.displayed_books = this.books.slice(0, this.itemsPerPage);
                this.filtered_books = []
            } else {
                const searchTextLowerCase = this.searchText.toLowerCase();
                let books = this.books.filter(book => {
                    return book.name.toLowerCase().includes(searchTextLowerCase);
                });
                this.filtered_books = books;
                this.displayed_books = this.filtered_books.slice(0, this.itemsPerPage)
            }
        },
        goToPage(pageNumber: number) {
            if (pageNumber >= 1 && pageNumber <= this.totalPages) {
                this.currentPage = pageNumber;
                const startIndex = (pageNumber - 1) * this.itemsPerPage;
                const endIndex = startIndex + this.itemsPerPage;
                if (this.filtered_books.length > 0) {
                    this.displayed_books = this.filtered_books.slice(startIndex, endIndex);
                } else {
                    this.displayed_books = this.books.slice(startIndex, endIndex);
                }
            }
        },
        showModal() {
            this.modalShow = true;
        },
        hideModal() {
            this.modalShow = false;
        },
        async fetchBooks() {
            const response = await this.$axios.get(this.url, {
                headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
            }).catch((err) => {
                console.log(err);
            });
            if (!response || response.status != 200) {
                console.error(response)
            } else {
                this.books = response.data
                this.displayed_books = this.books.slice(0, this.itemsPerPage);
            }
        },
        async fetchAuthors() {
            const response = await this.$axios.get(this.author_url, {
                headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
            }).catch((err) => {
                console.log(err);
            });
            if (!response || response.status != 200) {
                console.error(response)
            } else {
                for (let i = 0; i < response.data.length; i++) {
                    const element = response.data[i];
                    this.authors.push({ text: element.author, value: element.id })
                }
            }
        },
        async submitBook() {
            let response;
            if (this.actionType == "add") {
                response = await this.$axios.post(this.url,
                    {
                        name: this.bookName,
                        author_id: this.selectedAuthorId,
                        number_of_pages: this.number_of_pages
                    },
                    {
                        headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
                    }
                ).catch(err => console.log(err))
            } else if (this.actionType == "delete") {
                response = await this.$axios.delete(this.url + '/' + this.bookId,
                    {
                        headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
                    }
                ).catch(err => console.log(err))
            } else if (this.actionType == "update") {
                response = await this.$axios.put(this.url + '/' + this.bookId,
                    {
                        name: this.bookName,
                        author_id: this.selectedAuthorId,
                        number_of_pages: this.number_of_pages
                    },
                    {
                        headers: { "Authorization": "Bearer " + localStorage.getItem("fast_token") }
                    }
                ).catch(err => console.log(err))
            }
            if (response && response.status == 200) {
                this.fetchBooks();
            }
            this.bookName = "";
            this.bookId = 0;
        },
        addBook() {
            this.actionType = "add";
            this.showModal();
        },
        removeBook(id: any) {
            this.bookId = id;
            this.actionType = "delete";
            this.showModal()
        },
        updateBook(id: any) {
            let book = this.books.find(x => x.id == id);
            this.bookId = book?.id || 0;
            this.number_of_pages = book?.number_of_pages || 0;
            this.bookName = book?.name || "";
            this.selectedAuthorId = book?.author_id
            this.actionType = "update";
            this.showModal()
        }
    },
    async fetch() {
        await this.fetchBooks();
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