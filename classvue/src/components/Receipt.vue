<template>
  <HeaderC></HeaderC>
  <div class="flex flex-col items-center justify-center mt-4 min-h-screen bg-gray-50">
    <div class="items-center">
      <label class="text-base font-medium py-1 ml-4 sm:ml-0">Amount Received:</label>
      <input type="number" v-model="amount_received"
             class="border mx-4 w-3/4 sm:w-1/2 p-2 border-sky-300 outline-none rounded-md"><br>
      <label class="text-base font-medium py-1 mt-2 sm:mt-0 ml-4 sm:ml-0">Admission Date:</label>
      <input type="date" id="date" v-model="date"
             class="px-2 py-1 m-2 text-xl w-3/4 ml-4 sm:ml-0 sm:w-6/12 border border-sky-400 rounded-md outline-sky-500">
      <div class="sm:flex sm:items-center ml-4 sm:ml-0">
        <label class="text-base font-medium">Payment Received in:</label>
        <div class="">
          <input type="checkbox" value="Cash" id="cash" v-model="payment_rec" class="ml-2 mt-2">
          <label for="cash" class="text-base font-medium ml-2">Cash</label>
          <input type="checkbox" value="Online" id="online" v-model="payment_rec" class="ml-2 mt-2">
          <label for="online" class="text-base font-medium ml-2">Online</label>
          <input type="checkbox" value="Cheque" id="cheque" v-model="payment_rec" class="ml-2 mt-2">
          <label for="cheque" class="text-base font-medium ml-2">Cheque</label>
        </div>
      </div>
      <div class="mt-3">
        <label class="text-base font-medium py-1 ml-4 sm:ml-0">Received By: </label>
        <input type="text" v-model="received_by"
               class="border mx-4 w-3/4 sm:w-1/2 p-2 border-sky-300 outline-none rounded-md">
      </div>
    </div>
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
          <label class="text-base text-black font-normal">Date: {{ formatDate(date) }}</label>
        </div>
        <div class="text-start ml-2 mt-4">
          <label class="text-lg">Student Name: </label>
          <input class="text-lg w-1/2 border-0 border-b border-blue-500 outline-none" v-model="students.name"/>
        </div>
        <div class="text-start ml-2 mt-4">
          <label class="text-lg">Rs: </label>
          <input class="text-lg w-6/12 border-0 border-b border-blue-500 outline-none" v-model="amountInWords"/>
          <label class="text-lg">Std: </label>
          <input class="text-lg w-3/12 border-0 border-b border-blue-500 outline-none" v-model="students.std"/>
        </div>
        <div class="ml-2 mt-4">
          <table class="w-7/12 sm:w-4/12">
            <tr class="border-2 border-blue-500">
              <th class="p-2 border-r border-blue-500">
                <label class="text-base text-black font-normal border-b-0">Total Amount Due</label>
              </th>
              <th class="p-2">
                <label class="text-base text-black font-normal">{{ students.outstanding_fees }}</label>
              </th>
            </tr>
            <tr class="border-2 border-blue-500">
              <th class="p-2 border-r border-blue-500">
                <label class="text-base text-black font-normal border-b-0">Amount Received</label>
              </th>
              <th class="p-2">
                <label class="text-base text-black font-normal">{{ amount_received }}</label>
              </th>
            </tr>
            <tr class="border-2 border-blue-500">
              <th class="p-2 border-r border-blue-500">
                <label class="text-base text-black font-normal">Balance Due</label>
              </th>
              <th class="p-2">
                <label class="text-base text-black font-normal">{{ calculateDue }}</label>
              </th>
            </tr>
          </table>
        </div>
        <div class="sm:flex text-start ml-2 mt-4">
          <label class="text-base w-3/4 sm:w-6/12 text-black font-normal">Payment Received in: {{ payment_rec }}</label>
          <input
              class="border-0 border-b border-blue-400 w-6/12 sm:w-4/12 mr-2 sm:mr-0 ml-36 sm:ml-20 mt-2 sm:mt-0 text-center"
              v-model="received_by">
        </div>
        <div class="text-end mr-9 sm:mr-20">
          <label class="text-base text-black font-normal">Received By</label>
        </div>
      </div>
    </div>
    <button @click="printReceipt" type="button" class="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded-md mt-3">
      Download PDF
    </button>
    <button type="button" @click="updateFees" class="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded-md mt-3">
      Save
    </button>
  </div>
</template>

<script>
import axios from "axios";
import HeaderC from "@/components/Header.vue";
import html2pdf from "html2pdf.js";

export default {
  name: 'ReceiptM',
  data() {
    return {
      students: {
        name: '',
        std: '',
        total_fees: 0,
        paid_fees: 0,
        outstanding_fees: 0,
      },
      amount_received: 0,
      date: '',
      payment_rec: [],
      received_by: '',
      receipt_data: {},
    }
  },
  components: {
    HeaderC
  },
  computed: {
    calculateDue() {
      let total_fees = this.students.total_fees
      let paid_fees = this.students.paid_fees;
      let paid_now = parseInt(this.amount_received);
      let total_paid = paid_fees + paid_now;
      return total_fees - total_paid
    },
    totalPaidFees() {
      let paid_fees = this.students.paid_fees;
      let paid_now = parseInt(this.amount_received);
      return paid_fees + paid_now
    },
    amountInWords() {
      return this.convertToWords(this.amount_received)
    }
  },
  methods: {
    convertToWords(num) {
      if (!num) return '';

      const a = [
        '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
      ];
      const b = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];

      let result = '';

      if (num < 20) result = a[num];
      else if (num < 100) result = b[Math.floor(num / 10)] + (num % 10 ? ' ' + a[num % 10] : '');
      else if (num < 1000) result = a[Math.floor(num / 100)] + ' Hundred' + (num % 100 ? ' ' + this.convertToWords(num % 100) : '');
      else if (num < 100000) result = this.convertToWords(Math.floor(num / 1000)) + ' Thousand' + (num % 1000 ? ' ' + this.convertToWords(num % 1000) : '');
      else if (num < 10000000) result = this.convertToWords(Math.floor(num / 100000)) + ' Lakh' + (num % 100000 ? ' ' + this.convertToWords(num % 100000) : '');
      else if (num < 1000000000) result = this.convertToWords(Math.floor(num / 10000000)) + ' Crore' + (num % 10000000 ? ' ' + this.convertToWords(num % 10000000) : '');
      else return 'Number too large';

      return result.charAt(0).toUpperCase() + result.slice(1);
    },
    formatDate(date) {
      // Format date to DD-MM-YYYY
      if (!date) return '';
      const [year, month, day] = date.split('-');
      return `${day} / ${month} / ${year}`;
    },
    printReceipt() {
      const element = this.$refs.receiptContent;

      // Temporarily increase width for PDF
      const originalWidth = element.style.width;
      element.style.width = "100%";

      html2pdf()
          .from(element)
          .set({
            margin: 10,
            filename: `receipt_${this.students.name}.pdf`,
            image: {type: "jpeg", quality: 0.98},
            html2canvas: {scale: 2},
            jsPDF: {unit: "mm", format: "a4", orientation: "portrait"}
          })
          .save()
          .then(() => {
            // Revert width back after PDF is generated
            element.style.width = originalWidth;
          });
    },
    updateReceiptData() {
      this.receipt_data = {
        receipt_date: this.formatDate(this.date),
        stud_name: this.students.name,
        rs: this.amountInWords,
        std: this.students.std,
        tot_amount_due: this.students.outstanding_fees,
        amount_recived: this.amount_received,
        balance_due: this.calculateDue,
        payment_received_in: this.payment_rec,
        received_by: this.received_by
      }
    },
    async updateFees() {
      let paidf = this.totalPaidFees;
      let ot_fees = this.calculateDue;
      let sr = this.$route.params.id
      console.log("Sr = ", sr)
      this.updateReceiptData()
      console.log("Rec data", this.receipt_data)

      try {
        // Make sure the URL matches the one Django expects
        let result = await axios.patch('http://127.0.0.1:8000/api/Students/' + this.$route.params.id + '/', {
          paid_fees: paidf,
          outstanding_fees: ot_fees
        });

        let receipt = await axios.post('Receipt/', {
          sr: sr,
          receipt_date: this.receipt_data.receipt_date,
          stud_name: this.receipt_data.stud_name,
          rs: this.receipt_data.rs,
          std: this.receipt_data.std,
          tot_amount_due: this.receipt_data.tot_amount_due.toString(),  // Convert to string
          amount_recived: this.receipt_data.amount_recived.toString(),  // Convert to string
          balance_due: this.receipt_data.balance_due.toString(),        // Convert to string
          payment_received_in: this.receipt_data.payment_received_in.toString(), // Convert array to string
          received_by: this.receipt_data.received_by,
        });

        if (result.status === 200 &&  receipt.status === 201) {
          this.$router.push({name: 'Home'});
        }
      } catch (error) {
        console.error("Error during update:", error);
      }
    }

  },
  async mounted() {
    let response = await axios.get('Students/' + this.$route.params.id)
    this.students = response.data
  }
}
</script>

<style scoped>

</style>