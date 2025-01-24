<template>
<div class="bg-blue-300 h-screen flex justify-center items-center">
    <form @submit.prevent="loginUser">
        <div class="bg-white p-5 flex flex-col gap-0.5 w-96 rounded shadow-2xl">
            <img src="../assets/todo app icon.png" class="w-28 h-auto mx-auto mb-4" alt="">
            <p class="font-bold text-lg mb-4 text-center">Login</p>
            <input type="text" placeholder="Enter Username" id="username" v-model="username" class="border mx-4 w-80  p-2 border-sky-300 outline-sky-400 rounded-md">
            <br>
            <input type="password" placeholder="Enter Password" id="password" v-model="password" class="border  mx-4 w-80 p-2 border-sky-300 outline-sky-400 rounded-md">
            <br>
            <button type="submit" class="w-80 bg-sky-400 hover:bg-sky-500 mx-4 rounded-md p-2 text-white">Login</button>
            <div class="flex mt-2 gap-2 justify-center">
                <p class="text-md text-gray-900 bg-blu">{{ errorMessage }}</p>
            </div>
        </div>
    </form>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'LoginC',
    data() {
        return {
            username: '',
            password: '',
            errorMessage: '',  // Holds the error message for invalid credentials
        }
    },
    methods: {
        async loginUser() {
            try {
                let response = await axios.post('login/', {  // Update the URL if needed
                    username: this.username,
                    password: this.password,
                });

                if (response.status === 200) {
                    // Store user information in localStorage
                    localStorage.setItem("user-info", JSON.stringify(response.data));

                    // Redirect to the home page
                    this.$router.push('/home');
                } else {
                    // Handle unexpected responses
                    this.errorMessage = "An error occurred. Please try again later.";
                }

            } catch (error) {
                // Check if the error is a response from the server
                if (error.response && error.response.data && error.response.data.error) {
                    // Set the error message from the backend response
                    this.errorMessage = error.response.data.error;
                } else {
                    // Handle other unexpected errors
                    this.errorMessage = "Invalid credentials or server error.";
                }
                console.error("Login failed:", error);
            }
        },
    },
};
</script>

