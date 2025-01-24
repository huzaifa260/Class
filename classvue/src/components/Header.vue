<template>
<div class="flex gap-1 sm:gap-2 w-full bg-black p-4 sm:p-0 sm:h-16">
    <router-link to="/home" class="text-sm sm:text-xl text-gray-200 sm:ml-2 sm:pt-4 px-2 hover:bg-white hover:text-black">Home</router-link>
    <router-link to="/addstu" class="text-sm sm:text-xl text-gray-200 sm:ml-2 sm:pt-4 px-2 hover:bg-white hover:text-black">Add Student</router-link>
    <router-link to="" class="text-sm sm:text-xl text-gray-200 sm:ml-2 sm:pt-4 px-2 hover:bg-white hover:text-black">Receipt</router-link>
    <a href="" v-on:click="Logout" class="text-sm sm:text-xl text-gray-200 sm:ml-2 sm:pt-4 px-2 hover:bg-white hover:text-black">Logout</a>
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

</style>
