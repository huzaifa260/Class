<template>
  <HeaderC></HeaderC>
  <div v-for="i in receipt_data" :key="i">
    <div class="flex flex-col items-center justify-center mt-4 min-h-screen bg-gray-50">
      <div ref="receiptContent" id="receiptContent" class="bg-white shadow-md rounded-md mt-3 p-6 w-11/12 sm:w-6/12">
        <div class="py-5  border-2  border-blue-500 ">
          <label class="text-xl italic ml-2">SA</label>
        </div>
        <div class="py-3 flex border-2 border-t-0 border-blue-500 ">
          <label class="text-lg ml-2">
            First Floor, Chawre Manzil, Opposite Z.B. College, Sopara Gaon(West) 401203
          </label>
        </div>
        <div class="py-5  border-2 border-t-0 border-blue-500 text-center">
          <label class="text-2xl font-bold text-blue-950">Cash Receipt</label>
          <div class="text-end mr-5">
            <label class="text-base text-black font-normal">Date: </label>
          </div>
          <div class="text-start ml-2 mt-4">
            <label class="text-lg">Student Name: </label>
            <input class="text-lg w-1/2 border-0 border-b border-blue-500 outline-none"
                    :value="i.stud_name"/>
          </div>
          <div class="text-start ml-2 mt-4">
            <label class="text-lg">Rs: </label>
            <input class="text-lg w-6/12 border-0 border-b border-blue-500 outline-none" :value="i.rs" />
            <label class="text-lg">Std: </label>
            <input class="text-lg w-3/12 border-0 border-b border-blue-500 outline-none" :value="i.std"/>
          </div>
          <div class="ml-2 mt-4">
            <table class="w-7/12 sm:w-4/12">
              <tr class="border-2 border-blue-500">
                <th class="p-2 border-r border-blue-500">
                  <label class="text-base text-black font-normal border-b-0">Total Amount Due</label>
                </th>
                <th class="p-2">
                  <label class="text-base text-black font-normal">{{ i.tot_amount_due }}</label>
                </th>
              </tr>
              <tr class="border-2 border-blue-500">
                <th class="p-2 border-r border-blue-500">
                  <label class="text-base text-black font-normal border-b-0">Amount Received</label>
                </th>
                <th class="p-2">
                  <label class="text-base text-black font-normal">{{ i.amount_recived }} </label>
                </th>
              </tr>
              <tr class="border-2 border-blue-500">
                <th class="p-2 border-r border-blue-500">
                  <label class="text-base text-black font-normal">Balance Due</label>
                </th>
                <th class="p-2">
                  <label class="text-base text-black font-normal">{{ i.balance_due }} </label>
                </th>
              </tr>
            </table>
          </div>
          <div class="sm:flex text-start ml-2 mt-4">
            <label class="text-base w-3/4 sm:w-6/12 text-black font-normal">Payment Received in: {{ i.payment_received_in }}</label>
            <input
                class="border-0 border-b border-blue-400 w-6/12 sm:w-4/12 mr-2 sm:mr-0 ml-36 sm:ml-20 mt-2 sm:mt-0 text-center"
                :value="i.received_by"
            >
          </div>
          <div class="text-end mr-9 sm:mr-20">
            <label class="text-base text-black font-normal">Received By</label>
          </div>
        </div>
      </div>
      <button @click="printReceipt" type="button"
              class="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded-md mt-3">
        Download PDF
      </button>
      <button type="button" @click="updateFees" class="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded-md mt-3">
        Save
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import HeaderC from "@/components/Header.vue";

export default {
  name: 'ShowReceipts',
  components: {
    HeaderC
  },
  data() {
    return {
      receipt_data: [],
    }
  },
  methods: {
    async showReceipts() {
      // let sr = this.$route.params.id;
      let response = await axios.get('Students/' + this.$route.params.id)
      this.receipt_data = response.data
    }
  },
  mounted() {
    this.showReceipts()
  },
}
</script>

<style scoped>

</style>