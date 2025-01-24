<template>
<HeaderC></HeaderC>
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

        <tr v-for="(i, index) in students" :key="i" class="border-b border-slate-300 hover:bg-slate-100 text-center">
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
    components:{
        HeaderC
    },
    data() {
        return {
            students: [],
        }
    },
    methods:{
        async fetchData(){
            let result = await axios.get('Students/')
            this.students = result.data
            console.log(result.data)
        }
    },
    mounted(){
        this.fetchData()
    }
}
</script>
