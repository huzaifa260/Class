<template>
<div class="relative w-full bg-gradient-to-r from-gray-900 via-black to-gray-900 shadow-2xl">
    <div class="flex gap-2 sm:gap-4 w-full px-4 py-3 sm:px-6 items-center relative">

        <router-link
            to="/home"
            class="relative group text-sm sm:text-base text-gray-300 px-3 py-2 rounded-md transition-all duration-300 ease-out hover:text-white font-medium">
            <span class="relative z-10">Yearly Students</span>
            <div class="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-600 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </router-link>

        <router-link
            to="/monthlystudents"
            class="relative group text-sm sm:text-base text-gray-300 px-3 py-2 rounded-md transition-all duration-300 ease-out hover:text-white font-medium">
            <span class="relative z-10">Monthly Students</span>
            <div class="absolute inset-0 bg-gradient-to-r from-purple-500 to-pink-600 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </router-link>

        <router-link
            to="/addstu"
            class="relative group text-sm sm:text-base text-gray-300 px-3 py-2 rounded-md transition-all duration-300 ease-out hover:text-white font-medium">
            <span class="relative z-10">Add Student</span>
            <div class="absolute inset-0 bg-gradient-to-r from-green-500 to-emerald-600 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </router-link>

        <a
            href=""
            v-on:click="Logout"
            class="relative group text-sm sm:text-base text-gray-300 px-3 py-2 rounded-md transition-all duration-300 ease-out hover:text-white font-medium ml-auto">
            <span class="relative z-10">Logout</span>
            <div class="absolute inset-0 bg-gradient-to-r from-red-500 to-orange-600 rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </a>
    </div>

    <!-- Bottom accent line with animation -->
    <div class="h-0.5 w-full bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 animate-gradient"></div>
</div>
</template>

<script>
export default {
    name: 'HeaderC',
    methods: {
        Logout() {
            localStorage.clear();
            this.$router.push({
                name: 'Login2'
            })
            /* login details are stored in our localStorage so for logout we just clear the
            localStorage and redirect the user to login page so user will be log out */
        }
    }
}
</script>

<style scoped>
@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.animate-gradient {
    background-size: 200% 200%;
    animation: gradient 3s ease infinite;
}

/* Active route styling */
.router-link-active {
    @apply text-white;
}

.router-link-active::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    height: 2px;
    background: linear-gradient(to right, #3b82f6, #8b5cf6);
    border-radius: 2px;
}
</style>