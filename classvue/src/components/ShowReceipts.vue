<template>
  <HeaderC></HeaderC>
  <div class="min-h-screen bg-gray-50 py-6 px-4">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mr-2 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z" />
        </svg>
        Student Receipt History
      </h1>

      <div v-if="receipt_data.length === 0" class="text-center py-12">
        <p class="text-gray-500">No receipts found for this student</p>
      </div>

      <div v-for="(receipt, index) in receipt_data" :key="index" class="mb-8">
        <div ref="receiptContent" class="bg-white rounded-xl shadow-lg overflow-hidden">
          <!-- Receipt Header -->
          <div class="bg-gradient-to-r from-blue-600 to-blue-800 p-6 text-center">
            <h2 class="text-2xl font-bold text-white">Scholar's Academy</h2>
            <p class="text-blue-100 mt-1">First Floor, Chawre Manzil, Opposite Z.B. College, Sopara Gaon(West) 401203</p>
          </div>

          <!-- Receipt Body -->
          <div class="p-6">
            <div class="text-center mb-6">
              <h3 class="text-xl font-bold text-gray-800">OFFICIAL RECEIPT</h3>
              <p class="text-gray-500 text-sm">Receipt Date: {{ receipt.receipt_date }}</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
              <div>
                <label class="block text-sm font-medium text-gray-500">Student Name</label>
                <p class="text-lg font-semibold text-gray-800">{{ receipt.stud_name }}</p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-500">Class</label>
                <p class="text-lg font-semibold text-gray-800">{{ receipt.std }}</p>
              </div>
            </div>

            <!-- Yearly Fees Display -->
            <div v-if="receipt.tot_amount_due" class="mb-6">
              <label class="block text-sm font-medium text-gray-500 mb-2">Amount in Words</label>
              <p class="text-lg font-semibold text-gray-800 border-b-2 border-blue-200 pb-1">{{ receipt.rs }}</p>

              <div class="overflow-hidden rounded-lg border border-gray-200 shadow-sm mt-4">
                <table class="min-w-full divide-y divide-gray-200">
                  <thead class="bg-gray-50">
                    <tr>
                      <th class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
                      <th class="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase">Amount (₹)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td class="px-4 py-2 text-sm font-medium text-gray-900">Total Amount Due</td>
                      <td class="px-4 py-2 text-sm text-gray-500 text-right">{{ receipt.tot_amount_due || '0.00' }}</td>
                    </tr>
                    <tr class="bg-blue-50">
                      <td class="px-4 py-2 text-sm font-medium text-blue-800">Amount Received</td>
                      <td class="px-4 py-2 text-sm text-blue-800 font-bold text-right">{{ receipt.amount_recived || '0.00' }}</td>
                    </tr>
                    <tr>
                      <td class="px-4 py-2 text-sm font-medium text-gray-900">Balance Due</td>
                      <td class="px-4 py-2 text-sm text-gray-500 text-right">{{ receipt.balance_due || '0.00' }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Monthly Fees Display -->
            <div v-if="receipt.paid_months && receipt.paid_months.length > 0" class="mb-6">
              <label class="block text-sm font-medium text-gray-500">Monthly Fees Paid For:</label>
              <div class="flex flex-wrap gap-2 mt-2">
                <span
                  v-for="(month, idx) in formatPaidMonths(receipt.paid_months)"
                  :key="idx"
                  class="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-medium"
                >
                  {{ month }}
                </span>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
              <div>
                <label class="block text-sm font-medium text-gray-500">Payment Method</label>
                <p class="text-sm font-semibold text-gray-800">{{ formatPaymentMethods(receipt.payment_received_in) }}</p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-500">Received By</label>
                <p class="text-sm font-semibold text-gray-800">{{ receipt.received_by }}</p>
              </div>
            </div>
          </div>

          <!-- Receipt Footer -->
          <div class="px-6 py-4 border-t border-gray-200 text-center bg-gray-50 no-print">
            <button
              @click="printReceipt(index)"
              class="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              Download PDF
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import HeaderC from "@/components/Header.vue";
import * as htmlToImage from 'html-to-image'; // <-- The successful library
import jsPDF from 'jspdf';                     // <-- For creating the PDF

export default {
  name: 'ShowReceipts',
  components: {
    HeaderC
  },
  data() {
    return {
      receipt_data: [],
      student_info: {}
    }
  },
  methods: {
    async showReceipts() {
      try {
        const studentResponse = await axios.get(`Students/${this.$route.params.id}`);
        this.student_info = studentResponse.data;
        const receiptResponse = await axios.get(`Receipt/?sr=${this.$route.params.id}`);
        this.receipt_data = receiptResponse.data;
      } catch (error) {
        console.error("Error fetching receipts:", error);
      }
    },
    formatPaidMonths(months) {
      if (!months) return [];
      if (Array.isArray(months)) return months;
      try {
        // Attempt to parse if it's a JSON string array like '["June", "July"]'
        const parsed = JSON.parse(months);
        return Array.isArray(parsed) ? parsed : [months];
      } catch {
        // Fallback for a simple string
        return [months];
      }
    },
    formatPaymentMethods(methods) {
      if (!methods) return '';
      if (Array.isArray(methods)) {
        return methods.join(', ');
      }
      return methods.toString().replace(/[[\]"]+/g, '');
    },

    // FINAL PDF GENERATION METHOD using html-to-image
    printReceipt(index) {
      // Get the specific receipt element from the v-for loop
      const node = this.$refs.receiptContent[index];

      const options = {
        pixelRatio: 3, // Use a high pixel ratio for a crisp, high-resolution image
        backgroundColor: '#ffffff',
        // This function tells the library to ignore any element with the 'no-print' class
        filter: (element) => {
          return element.classList ? !element.classList.contains('no-print') : true;
        }
      };

      htmlToImage.toPng(node, options)
        .then((dataUrl) => {
          const doc = new jsPDF('p', 'mm', 'a4');
          const pdfWidth = doc.internal.pageSize.getWidth();
          const margin = 10;
          const imgWidth = pdfWidth - (margin * 2);

          const imgProps = doc.getImageProperties(dataUrl);
          const imgHeight = (imgProps.height * imgWidth) / imgProps.width;

          doc.addImage(dataUrl, 'PNG', margin, margin, imgWidth, imgHeight);
          doc.save(`Receipt_${this.receipt_data[index].stud_name}.pdf`);
        })
        .catch((error) => {
          console.error('PDF Generation Error:', error);
        });
    }
  },
  mounted() {
    this.showReceipts();
  }
}
</script>

<style scoped>
/* Animation for receipt cards */
.receipt-enter-active {
  transition: all 0.3s ease;
}
.receipt-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

/* Print styles */
@media print {
  body * {
    visibility: hidden;
  }
  .receipt-content, .receipt-content * {
    visibility: visible;
  }
  .receipt-content {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    margin: 0;
    padding: 0;
  }
  .no-print {
    display: none !important;
  }
}

/* Ensure proper spacing for monthly fees tags in PDF */
span {
  page-break-inside: avoid;
}
</style>