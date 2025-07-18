<template>
  <HeaderC></HeaderC>

  <!-- Filter Section with Animation -->
  <div class="flex mt-8 container mx-auto gap-4 px-4 animate-fade-in">
    <label for="classFilter" class="text-gray-700 font-medium self-center">Filter by Class:</label>
    <select
        v-model="selectedClass"
        class="rounded-lg border-2 border-gray-300 px-4 py-2 focus:border-rose-500 focus:ring-rose-500 transition-all duration-300 shadow-sm hover:shadow-md"
    >
      <option value="All">All Classes</option>
      <option v-for="std in uniqueClasses" :key="std" :value="std">{{ std }}</option>
    </select>
  </div>

  <!-- Table Container with Enhanced Styling -->
  <div class="container mx-auto px-4 py-6 animate-slide-up">
    <div class="bg-white rounded-xl shadow-xl overflow-hidden transition-all duration-300 hover:shadow-2xl">
      <table class="w-full min-w-max">
        <!-- Table Header -->
        <thead>
        <tr class="bg-gradient-to-r from-rose-600 to-rose-500 text-white">
          <th class="text-xl p-6 text-left font-bold" colspan="8">
            <div class="flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mr-3" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
              </svg>
              Monthly Student Records
            </div>
          </th>
        </tr>
        <tr class="bg-gray-100 text-gray-700 font-semibold text-sm uppercase tracking-wider">
          <th class="p-4 text-left">S.N</th>
          <th class="p-4 text-left">Name</th>
          <th class="p-4 text-left">Class</th>
          <th class="p-4 text-left">Admission Date</th>
          <th class="p-4 text-left">Monthly Fees</th>
          <th class="p-4 text-left">Paid Months</th>
          <th class="p-4 text-left">Actions</th>
        </tr>
        </thead>

        <!-- Table Body with Hover Effects -->
        <tbody class="divide-y divide-gray-200">
        <tr
            v-for="(i, index) in filteredStudents"
            :key="i.id"
            class="transition-all duration-200 hover:bg-rose-50 hover:scale-[1.01]"
        >
          <td class="p-4 font-medium text-gray-900">{{ index + 1 }}</td>
          <td class="p-4">
            <div class="flex items-center">
              <div class="flex-shrink-0 h-10 w-10 rounded-full bg-rose-100 flex items-center justify-center mr-3">
                <span class="text-rose-600 font-medium">{{ i.name.charAt(0) }}</span>
              </div>
              <div>
                <div class="font-medium text-gray-900">{{ i.name }}</div>
                <div class="text-gray-500 text-sm">ID: {{ i.id }}</div>
              </div>
            </div>
          </td>
          <td class="p-4">
              <span class="px-3 py-1 rounded-full text-sm font-medium bg-rose-100 text-rose-800">
                {{ i.std }}
              </span>
          </td>
          <td class="p-4 text-gray-700">{{ formatDate(i.admission_date) }}</td>
          <td class="p-4 font-medium text-gray-900">₹{{ i.total_fees }}</td>
          <td class="p-4 text-green-600 font-medium">₹{{ i.paid_fees }}</td>
          <td class="p-4 space-x-2">
            <router-link
                :to="'/receipt/' + i.id"
                class="inline-flex items-center px-4 py-2 bg-rose-600 text-white rounded-lg hover:bg-rose-700 transition-colors duration-300 shadow-sm"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z"/>
              </svg>
              Receipt
            </router-link>
            <router-link
                :to="'/showreceipts/' + i.id"
                class="inline-flex items-center px-4 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition-colors duration-300 shadow-sm"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24"
                   stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              History
            </router-link>
          </td>
        </tr>
        </tbody>
      </table>

      <!-- Empty State -->
      <div v-if="filteredStudents.length === 0" class="p-12 text-center text-gray-500">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-300" fill="none" viewBox="0 0 24 24"
             stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <h3 class="mt-4 text-lg font-medium">No students found</h3>
        <p class="mt-1">Try adjusting your filters or add new students</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import HeaderC from './Header.vue';

export default {
  name: 'MonthlyStudents',
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
      let result = await axios.get('Students/?fees_type=monthly');
      this.students = result.data;

    },
    formatDate(dateString) {
      // Add date formatting logic if needed
      return dateString
    }
  },
  mounted() {
    this.fetchData()
  }
}
</script>
<style scoped>
/* Animation Classes */
.animate-fade-in {
  animation: fadeIn 0.5s ease-out;
}

.animate-slide-up {
  animation: slideUp 0.6s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Hover effects for table rows */
tr:hover {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

/* Custom scrollbar for table (if it becomes scrollable) */
.table-container::-webkit-scrollbar {
  height: 8px;
  width: 8px;
}

.table-container::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}

.table-container::-webkit-scrollbar-thumb {
  background: #e11d48;
  border-radius: 10px;
}

.table-container::-webkit-scrollbar-thumb:hover {
  background: #be123c;
}
</style>
