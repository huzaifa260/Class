<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-purple-50 to-indigo-100 animate-gradient">
    <form
      @submit.prevent="submitLogin"
      class="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md border border-gray-100 transform transition-all duration-500 hover:shadow-2xl"
    >
      <div class="text-center mb-8 animate-fade-in-down">
        <h2 class="text-3xl font-bold text-gray-800 mb-2">Welcome Back</h2>
        <p class="text-gray-500 animate-pulse">Login to your account</p>
      </div>

      <div class="space-y-5">
        <div class="animate-fade-in-up" style="animation-delay: 0.1s">
          <label for="username" class="block text-sm font-medium text-gray-700 mb-1">Username</label>
          <input
            v-model="username"
            id="username"
            type="text"
            placeholder="Enter your username"
            class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all duration-300 hover:border-blue-400"
          />
        </div>

        <div class="animate-fade-in-up" style="animation-delay: 0.2s">
          <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
          <input
            v-model="password"
            id="password"
            type="password"
            placeholder="Enter your password"
            class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all duration-300 hover:border-blue-400"
          />
        </div>

        <p
          v-if="error"
          class="text-red-500 text-sm py-2 px-3 bg-red-50 rounded-lg animate-shake"
        >
          {{ error }}
        </p>

        <button
          type="button" @click="Login"
          class="w-full bg-gradient-to-r from-blue-500 to-pink-500 text-white py-3 rounded-lg font-semibold shadow-lg hover:from-blue-600 hover:to-pink-600 transition-all duration-300 hover:scale-[1.02] focus:outline-none focus:ring-4 focus:ring-blue-300/50 active:scale-95"
        >
          <span class="inline-block transform transition-transform duration-200 group-hover:translate-x-1">
            Login
          </span>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginC2',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async Login() {
      let result = await axios.get(
          `/User?name=${this.username}&password=${this.password}`
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
<style scoped >
@keyframes gradient {
  0% { background-position: 0 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0 50%; }
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
  20%, 40%, 60%, 80% { transform: translateX(5px); }
}

.animate-gradient {
  background-size: 200% 200%;
  animation: gradient 10s ease infinite;
}

.animate-fade-in-down {
  animation: fadeInDown 0.6s ease-out forwards;
}

.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
}

.animate-shake {
  animation: shake 0.5s ease-in-out;
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
</style>