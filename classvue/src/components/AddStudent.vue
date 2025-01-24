<template>
  <HeaderC></HeaderC>
  <div class="flex flex-col gap-3 items-center">
    <label class="mt-10 text-2xl font-medium px-2 py-1">Student Details</label>
    <input type="text" placeholder="Student Name" v-model="stud_name" id="stud_name"
           class="px-2 py-1 m-2 text-xl w-3/4 sm:w-3/12 border border-sky-400 rounded-md outline-sky-500">
    <input type="text" placeholder="Standard" v-model="std" id="std"
           class="px-2 py-1 m-2 text-xl w-3/4 sm:w-3/12 border border-sky-400 rounded-md outline-sky-500">
    <input type="number" placeholder="Fees" v-model="fees" id="fees"
           class="px-2 py-1 m-2 text-xl w-3/4 sm:w-3/12 border border-sky-400 rounded-md outline-sky-500">
    <label class="text-lg font-medium px-2 py-1">Admission Date:</label>
    <input type="date" id="admission_date" v-model="admission_date"
           class="px-2 py-1 m-2 text-xl w-3/4 sm:w-3/12 border border-sky-400 rounded-md outline-sky-500">
    <button type="button" v-on:click="addStud"
            class="w-3/4 sm:w-3/12 bg-sky-400 hover:bg-sky-500 mx-4 rounded-md p-2 text-white">Add
    </button>
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
      paid_fees: 0,
      admission_date: '',
      sr:null,
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

      let response = await axios.post('Students/', {
        sr:this.sr,
        name: this.stud_name,
        std: this.std,
        total_fees: this.fees,
        paid_fees: this.paid_fees,
        outstanding_fees: this.fees,
        admission_date: date
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

</style>