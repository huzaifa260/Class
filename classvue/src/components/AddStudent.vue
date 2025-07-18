<template>
  <HeaderC></HeaderC>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 py-10 px-4">
    <div class="max-w-md mx-auto bg-white rounded-xl shadow-2xl overflow-hidden animate-fade-in">
      <!-- Header Section -->
      <div class="bg-gradient-to-r from-blue-600 to-blue-700 p-6 text-center">
        <h1 class="text-3xl font-bold text-white flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mr-2" fill="none" viewBox="0 0 24 24"
               stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
          </svg>
          Add New Student
        </h1>
      </div>

      <!-- Form Section -->
      <div class="p-6 space-y-6">
        <!-- Student Name -->
        <div class="space-y-1">
          <label for="stud_name" class="block text-sm font-medium text-gray-700">Student Name</label>
          <div class="relative">
            <input
                type="text"
                id="stud_name"
                v-model="stud_name"
                placeholder="Enter student name"
                class="w-full px-4 py-3 outline-none border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 pl-10"
            >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 absolute left-3 top-3.5" fill="none"
                 viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
            </svg>
          </div>
        </div>

        <!-- Standard -->
        <div class="space-y-1">
          <label for="std" class="block text-sm font-medium text-gray-700">Standard</label>
          <div class="relative">
            <input
                type="text"
                id="std"
                v-model="std"
                placeholder="Enter class/standard"
                class="w-full px-4 py-3 outline-none border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 pl-10"
            >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 absolute left-3 top-3.5" fill="none"
                 viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
            </svg>
          </div>
        </div>

        <!-- Fee Type -->
        <div class="space-y-1">
          <label for="feeType" class="block text-sm font-medium text-gray-700">Fees Type</label>
          <div class="relative">
            <select
                id="feeType"
                v-model="feeType"
                class="w-full px-4 py-3 outline-none border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 pl-10"
            >
              <option disabled value="">Select type</option>
              <option value="yearly">Yearly</option>
              <option value="monthly">Monthly</option>
            </select>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 absolute left-3 top-3.5" fill="none"
                 viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </div>
        </div>


        <!-- Fees -->
        <div class="space-y-1">
          <label for="fees" class="block text-sm font-medium text-gray-700">Fees (₹)</label>
          <div class="relative">
            <input
                type="number"
                id="fees"
                v-model="fees"
                placeholder="Enter fees amount"
                class="w-full px-4 py-3 outline-none border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 pl-10"
            >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 absolute left-3 top-3.5" fill="none"
                 viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>

        <!-- Admission Date -->
        <div class="space-y-1">
          <label for="admission_date" class="block text-sm font-medium text-gray-700">Admission Date</label>
          <div class="relative">
            <input
                type="date"
                id="admission_date"
                v-model="admission_date"
                class="w-full px-4 py-3 outline-none border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 pl-10"
            >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 absolute left-3 top-3.5" fill="none"
                 viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
          </div>
        </div>

        <!-- Submit Button -->
        <button
            @click="addStud"
            class="w-full py-3 px-4 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-medium rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:scale-[1.02] flex items-center justify-center"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
               stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
          </svg>
          Add Student
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import HeaderC from "@/components/Header.vue";
import axios from "axios";

export default {
  name: 'AddStudent',
  data() {
    return {
      stud_name: '',
      std: '',
      fees: '',
      feeType: '',
      paid_fees: 0,
      admission_date: '',
      sr: null,
    }
  },
  components: {
    HeaderC
  },
  methods: {
    formatDate(date) {
      // Format date to DD-MM-YYYY
      if (!date) return '';
      const [year, month, day] = date.split('-');
      return `${day}-${month}-${year}`;
    },
    getAdmissionMonth() {
      if (!this.admission_date) return "";
      const date = new Date(this.admission_date);
      // List of month names in English
      const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
      ];
      // getMonth() returns 0-based index
      return months[date.getMonth()];
    },
    async fetchMaxSR() {
      try {
        const response = await axios.get('/get_max_sr/');
        this.sr = response.data.max_sr;  // Set the sr value in the component
        console.log("Sr = ", this.sr)
      } catch (error) {
        console.error("Error fetching SR:", error);
      }
    },
    async addStud() {
      let date = this.formatDate(this.admission_date)
      let starting_month = this.getAdmissionMonth()

      let response = await axios.post('Students/', {
        sr: this.sr,
        name: this.stud_name,
        std: this.std,
        fees_type: this.feeType,
        total_fees: this.fees,
        paid_fees: this.paid_fees,
        outstanding_fees: this.fees,
        admission_date: date,
        starting_month: starting_month,
      });
      /* here we add the student with post method we send data to api and it gets stored */
      if (response.status === 201) {
        this.$router.push({name: 'Home'})
      }

    }
  }
}
</script>

<style scoped>
/* Animation Classes */
.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Input focus effect */
input:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

/* Date input custom styling */
input[type="date"]::-webkit-calendar-picker-indicator {
  background: transparent;
  bottom: 0;
  color: transparent;
  cursor: pointer;
  height: auto;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  width: auto;
}
</style>