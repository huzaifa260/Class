<template>
  <HeaderC></HeaderC>
  <div
      class="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 py-8 px-4">
    <!-- Form Section with Animation -->
    <div class="bg-white rounded-xl shadow-lg p-6 w-full max-w-2xl mb-8 animate-fade-in">
      <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mr-2 text-blue-600" fill="none" viewBox="0 0 24 24"
             stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z"/>
        </svg>
        Payment Details
        {{ selected_months }}
      </h2>

      <div class="space-y-4">
        <div v-if="students.fees_type === 'monthly'">
          <label class="block text-sm font-medium text-gray-700 mb-1">Select Month(s)</label>
          <div class="flex flex-wrap gap-4">
            <label v-for="m in availableMonths" :key="m" class="inline-flex items-center">
              <input
                  type="checkbox"
                  :value="m"
                  v-model="selected_months"
                  class="h-5 w-5 text-blue-600 rounded focus:ring-blue-500 transition-all duration-200"
              >
              <span class="ml-2 text-gray-700">{{ m }}</span>
            </label>
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

          <div v-if="students.fees_type === 'yearly'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Amount Received (₹)</label>
            <input
                type="number"
                v-model="amount_received"
                class="w-full px-4 py-2 border border-gray-300 outline-none rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300"
                placeholder="Enter amount"
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Receipt Date</label>
            <input
                type="date"
                id="date"
                v-model="date"
                class="w-full px-4 py-2 border border-gray-300 outline-none rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300"
            >
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Payment Method</label>
          <div class="flex flex-wrap gap-4">
            <label class="inline-flex items-center">
              <input
                  type="checkbox"
                  value="Cash"
                  id="cash"
                  v-model="payment_rec"
                  class="h-5 w-5 text-blue-600 rounded focus:ring-blue-500 transition-all duration-200"
              >
              <span class="ml-2 text-gray-700">Cash</span>
            </label>
            <label class="inline-flex items-center">
              <input
                  type="checkbox"
                  value="Online"
                  id="online"
                  v-model="payment_rec"
                  class="h-5 w-5 text-blue-600 rounded focus:ring-blue-500 transition-all duration-200"
              >
              <span class="ml-2 text-gray-700">Online</span>
            </label>
            <label class="inline-flex items-center">
              <input
                  type="checkbox"
                  value="Cheque"
                  id="cheque"
                  v-model="payment_rec"
                  class="h-5 w-5 text-blue-600 rounded focus:ring-blue-500 transition-all duration-200"
              >
              <span class="ml-2 text-gray-700">Cheque</span>
            </label>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Received By</label>
          <select
              v-model="received_by"
              class="w-full px-4 py-2 outline-none border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300"
          >
            <option value="" disabled selected>Select receiver</option>
            <option v-for="receiver in receivers" :key="receiver" :value="receiver">
              {{ receiver }}
            </option>
          </select>
        </div>
      </div>
    </div>

    <!-- Receipt Preview with Animation -->
    <div
        ref="receiptContent"
        id="receiptContent"
        class="bg-white shadow-xl rounded-xl overflow-hidden w-full max-w-2xl animate-slide-up"
    >
      <!-- Receipt Header -->
      <div class="bg-gradient-to-r from-blue-600 to-blue-800 p-6 text-center">
        <div class="flex justify-center items-center mb-2">
          <div class="bg-white rounded-full p-3 shadow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-blue-600" fill="none" viewBox="0 0 24 24"
                 stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z"/>
            </svg>
          </div>
        </div>
        <h1 class="text-3xl font-bold text-white">Scholars Academy</h1>
        <p class="text-blue-100 mt-2">First Floor, Chawre Manzil, Opposite Z.B. College, Sopara Gaon(West) 401203</p>
      </div>

      <!-- Receipt Body -->
      <div class="p-6">
        <div class="text-center mb-8">
          <h2 class="text-2xl font-bold text-gray-800">OFFICIAL RECEIPT</h2>
          <p class="text-gray-500 mt-1">Date: {{ formatDate(date) }}</p>
        </div>

        <div class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-500">Student Name</label>
              <div class="mt-1 text-lg font-semibold text-gray-800 border-b-2 border-blue-200 pb-1">
                {{ students.name || "________________" }}
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-500">Class</label>
              <div class="mt-1 text-lg font-semibold text-gray-800 border-b-2 border-blue-200 pb-1">
                {{ students.std || "____" }}
              </div>
            </div>
          </div>

          <div v-if="students.fees_type === 'yearly'">
            <label class="block text-sm font-medium text-gray-500">Amount in Words</label>
            <div class="mt-1 text-lg font-semibold text-gray-800 border-b-2 border-blue-200 pb-1">
              {{ amountInWords }}
            </div>
          </div>

          <!-- Payment Summary Table -->
          <div v-if="students.fees_type === 'yearly'"
               class="overflow-hidden rounded-lg border border-gray-200 shadow-sm">

            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Description
                </th>
                <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Amount (₹)
                </th>
              </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
              <tr>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Total Amount Due</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-right">
                  {{ students.outstanding_fees || "0.00" }}
                </td>
              </tr>
              <tr class="bg-blue-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-blue-800">Amount Received</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-blue-800 font-bold text-right">
                  {{ amount_received || "0.00" }}
                </td>
              </tr>
              <tr>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Balance Due</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-right">{{
                    calculateDue || "0.00"
                  }}
                </td>
              </tr>
              </tbody>
            </table>
          </div>
          <div v-if="students.fees_type === 'monthly'">
            <!-- Label -->
            <label class="block text-sm font-medium text-gray-500">Monthly Fees</label>
            <div class="mb-2 text-lg font-semibold text-gray-800">
              ₹{{ students.total_fees || students.monthly_fees || "0.00" }} per month
            </div>

            <!-- Paid Months (selected by user) -->
            <label class="block text-sm font-medium text-gray-500">Month(s) Paid:</label>
            <div class="flex flex-wrap gap-2 my-2">
            <span v-for="m in selected_months" :key="m"
                  class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm font-semibold border border-blue-300">
                {{ m }}
            </span>
              <span v-if="selected_months.length === 0" class="text-gray-400 text-sm">
                No months selected
            </span>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
            <div>
              <label class="block text-sm font-medium text-gray-500">Payment Method</label>
              <div class="mt-1 text-lg font-semibold text-gray-800">
                {{ payment_rec.join(", ") }}
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-500">Received By</label>
              <div class="mt-1 text-lg font-semibold text-gray-800 border-b-2 border-blue-200 pb-1">
                {{ received_by }}
              </div>
            </div>
          </div>
        </div>

        <!-- Receipt Footer -->
        <div class="mt-12 pt-6 border-t border-gray-200 text-center">
          <p class="mt-8 text-xs text-gray-400">Thank you for your payment. This is a computer generated receipt and
            does not require a physical signature.</p>
        </div>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="flex flex-wrap justify-center gap-4 mt-8 animate-fade-in">
      <button
          @click="printReceipt"
          class="flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
             stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
        </svg>
        Download PDF
      </button>
      <button
          @click="updateFees"
          class="flex items-center px-6 py-3 bg-gradient-to-r from-green-600 to-green-700 text-white rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
             stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
        </svg>
        Save Receipt
      </button>
    </div>
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
        fees_type: '',
        total_fees: 0,
        paid_fees: 0,
        outstanding_fees: 0,
      },
      amount_received: 0,
      date: '',
      payment_rec: [],
      received_by: '',
      receivers: ['Tauseef', 'Maqsood', 'Nusrat'],
      receipt_data: {},
      start_month: '',     // admission month as string, e.g., "July"
      paid_months: [],
      selected_months: [],
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
    },
    availableMonths() {
      if (this.students.fees_type !== 'monthly' || !this.start_month) return [];

      const months_full = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
      ];

      const startIdx = months_full.indexOf(this.start_month);
      if (startIdx === -1) return [];

      let months = [];
      if (startIdx <= 3) {
        // Jan (0), Feb (1), Mar (2), Apr (3)
        // So: from start month to April **of this year**
        for (let i = startIdx; i <= 3; i++) {
          months.push(months_full[i]);
        }
      } else {
        // Start after April (May–Dec): from startMonth to December, *then* Jan–April next year
        for (let i = startIdx; i < 12; i++) {
          months.push(months_full[i]);
        }
        for (let i = 0; i <= 3; i++) {
          months.push(months_full[i]);
        }
      }

      // Exclude paid months
      if (this.paid_months && Array.isArray(this.paid_months)) {
        months = months.filter(m => !this.paid_months.includes(m));
      }
      return months;
    },
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

    formatMonth(m) {
      const [year, month] = m.split("-");
      const monthNames = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
      ];
      return `${monthNames[Number(month) - 1]} ${year}`;
    },
    updateReceiptData() {
      if (this.students.fees_type === 'monthly') {
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
        };
        // Save or further processing here
      } else {
        // Handle other fees types or do nothing
        this.receipt_data = {
          receipt_date: this.formatDate(this.date),
          stud_name: this.students.name,
          rs: this.amountInWords,
          std: this.students.std,
          paid_months: this.selected_months,
          payment_received_in: this.payment_rec,
          received_by: this.received_by
        }
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
        if (this.students.fees_type === 'yearly') {
          await axios.patch('http://127.0.0.1:8001/api/Students/' + this.$route.params.id + '/', {
            paid_fees: paidf,
            outstanding_fees: ot_fees
          });
        } else {
          let updatedPaidMonths = this.paid_months.concat(this.selected_months)
          // we first take paid months and add currently paid months in it
          await axios.patch('http://127.0.0.1:8001/api/Students/' + this.$route.params.id + '/', {
            paid_months: updatedPaidMonths,
          });
        }

        await axios.post('Receipt/', {
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
        this.$router.push({name: 'Home'});

      } catch (error) {
        console.error("Error during update:", error);
      }
    }

  },
  async mounted() {
    let response = await axios.get('Students/' + this.$route.params.id)
    this.students = response.data
    this.start_month = response.data.starting_month || 'July'  // Fallback for demo
    this.paid_months = response.data.paid_months || [];
  }
}
</script>

<style scoped>
/* Animation Classes */
.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
}

.animate-slide-up {
  animation: slideUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
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
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media print {
  * {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
}

#receiptContent {
  background: white;
}


/* Print-specific styles */
@media print {
  body * {
    visibility: hidden;
  }

  #receiptContent, #receiptContent * {
    visibility: visible;
  }

  #receiptContent {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    margin: 0;
    padding: 0;
    box-shadow: none;
  }

  .no-print {
    display: none !important;
  }
}
</style>