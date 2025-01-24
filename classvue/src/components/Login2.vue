<template>
  <div class="bg-blue-300 h-screen flex justify-center items-center">
    <div class="bg-white p-5 flex flex-col gap-0.5 w-96 rounded shadow-2xl">
      <img src="../assets/todo app icon.png" class="w-28 h-auto mx-auto mb-4" alt="">
      <p class="font-bold text-lg mb-4 text-center">Login</p>
      <input type="text" placeholder="Enter Username" v-model="name"
             class="border mx-4 w-80  p-2 border-sky-300 outline-sky-400 rounded-md">
      <br>
      <input type="password" placeholder="Enter Password" v-model="Password"
             class="border  mx-4 w-80 p-2 border-sky-300 outline-sky-400 rounded-md">
      <br>
      <button type="button" v-on:click="Login" class="w-80 bg-sky-400 hover:bg-sky-500 mx-4 rounded-md p-2 text-white">
        Login
      </button>
      <div class="flex mt-2 gap-2 justify-center">
        <p class="text-md text-gray-900 bg-blu">{{ errorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginC2',
  data() {
    return {
      name: '',
      Password: '',
    }
  },
  methods: {
    async Login() {
      let result = await axios.get(
          `/User?name=${this.name}&password=${this.Password}`
      );
      // http://localhost:3000/user?email=hzr@test.com&password=123
      console.log(result.data)
      if (result.status === 200 && result.data.length > 0) {
        localStorage.setItem("user-info", JSON.stringify(result.data[0]))
        await this.$router.push({
          name: "Home"
        })
      }
    }
  },
  mounted() {
    let user = localStorage.getItem("user-info");
    if (user) {
      this.$router.push({name: "Home"})
    }
  }
}
</script>
    