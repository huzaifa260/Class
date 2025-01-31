<template>
  <h2>Sun</h2>
</template>

<script>
import axios from "axios";

export default {
  name: 'ShowReceipts',
  data() {
    return {
      receipt_data: [],
    }
  },
  methods: {
    async showReceipts() {
      let sr = this.$route.params.id;
      console.log("Sr =", sr)
      let response = await axios.get(`Receipt/?sr=${sr}`)
      console.log("Data =", response.data)
    }
  },
  mounted() {
    this.showReceipts()
  },
}
</script>

<style scoped>

</style>