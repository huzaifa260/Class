<template>
  <HeaderC></HeaderC>
  <div class="flex mt-4 container mx-auto gap-2">
    <label for="classFilter">Filter by Class:</label>
    <select v-model="selectedClass" class="rounded-md border-2 border-slate-800">
      <option value="All">All</option>
      <option v-for="std in uniqueClasses" :key="std" :value="std">{{ std }}</option>
    </select>
  </div>
  <div class="flex w-full shadow-lg rounded-lg bg-clip-border mt-4 container mx-auto">
    <table class="w-full table-auto">
      <tr class="border-b border-slate-300 bg-rose-600 text-white">
        <th class="text-xl p-2" colspan="8">Students</th>
      </tr>
      <tr class="border-b border-slate-300 hover:bg-slate-100">
        <th class="p-2">S.N</th>
        <th class="p-2">Name</th>
        <th class="p-2">Std</th>
        <th class="p-2">Admission Date</th>
        <th class="p-2">Total Fees</th>
        <th class="p-2">Paid</th>
        <th class="p-2">Outstanding</th>
        <th class="p-2">Receipt</th>
      </tr>

      <tr v-for="(i, index) in filteredStudents" :key="i"
          class="border-b border-slate-300 hover:bg-slate-100 text-center">
        <td class="p-2">{{ index + 1 }}</td>
        <td class="p-2">{{ i.name }}</td>
        <td class="p-2">{{ i.std }}</td>
        <td class="p-2">{{ i.admission_date }}</td>
        <td class="p-2">{{ i.total_fees }}</td>
        <td class="p-2">{{ i.paid_fees }}</td>
        <td class="p-2">{{ i.outstanding_fees }}</td>
        <td class="p-2">
          <router-link :to="'/receipt/'+i.id">
            <button type="button" class="px-3 bg-sky-400 rounded-3xl text-white">Receipt</button>
          </router-link>
          <router-link :to="'/showreceipts/'+i.id">
            <button type="button" class="px-3 bg-sky-400 rounded-3xl text-white">Show Receipts</button>
          </router-link>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
import HeaderC from './Header.vue';

export default {
  name: 'HomePage',
  components: {
    HeaderC
  },
  data() {
    return {
      students: [],
      selectedClass: "All",  // Default selected option
      selectedName: "",  // Filter by name (empty means no filter)
      selectedOutstandingFees: null,  // Filter by outstanding fees (empty means no filter)
    }
  },
  computed: {
    uniqueClasses() {
      const classes = new Set(this.students.map(student => student.std));
      /* 'this.students.map(student => student.std' with map() we can make array from a object
      like here we have remove only std values from object using map method
      now we want only unique values so for that reason this array is converted into set to
      store unique values and to create Set we need to initialize it by instance like here we
      have done 'const classes = new' classes is the instance for Set()   */

      return [...classes].sort(); // Convert to array & sort
      /* [...classes] converts Set object into array and than we sort it */

      /* first we create a array of all std's available han passed/convert it to Set to fetch
      unique values and than converted that Set into array and sort it */
    },
    // Filter students based on the selected class
    filteredStudents() {
      if (this.selectedClass === "All") {
        return this.students;
      }
      return this.students.filter(student => student.std === this.selectedClass);
    }
  },
  methods: {
    async fetchData() {
      let result = await axios.get('Students/')
      this.students = result.data
    }
  },
  mounted() {
    this.fetchData()
  }
}
</script>
