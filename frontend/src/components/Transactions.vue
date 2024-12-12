<script>
import { onMounted } from "vue";
import { useTransactionStore } from "../stores/transaction";

export default {
  name: "Transactions",
  data() {
    storeTransaction: { }
  },
  methods: {
    fetchPost() {
      this.storeTransaction.fetchData();
    },
  },
  created() {
    this.storeTransaction = useTransactionStore();
    this.fetchPost();
  },
};
</script>

<template>
  <div>
    <div v-if="modalOpen"
      class="w-full h-screen bg-[rgb(255,255,255,0.4)] flex items-center justify-center fixed top-0 left-0 z-50">
      <div class="bg-gray-800 p-8 rounded-md">
        <h2 class="text-xl text-white">Modal Content</h2>
        <p class="text-white">You double-clicked a transaction!</p>
        <button @click="" class="mt-4 text-white bg-red-500 rounded px-4 py-2">
          Close Modal
        </button>
      </div>
    </div>
    <!-- <Modal /> -->

    <!-- <Navbar> -->
    <main class="h-full w-full">
      <div class="w-full flex justify-between p-4 bg-white shadow-md rounded-md mb-6">
        <div class="flex gap-8 items-center">
          <!-- Label & Check Box -->
          <label 
            class="flex items-center gap-2 text-gray-700">
            <input type="checkbox" 
              class="h-5 w-5" />
           
          </label>
          <button @click="">+ Add new</button>
        </div>
        <div class="flex flex-col items-center justify-center">
          <div class="text-gray-600">
            <!-- User ID -->
          </div>
          <button @click="" class="mt-4 py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600">
            Logout
          </button>
        </div>
      </div>
      <!-- <Navbar /> -->

      <!-- Card -->
      <div class="flex gap-1 w-full h-full">
        <div>
          <!-- if exceed card will turn red -->
          <div class="w-[240px] h-full space-y-4 p-4 bg-white shadow-md rounded-md">
            <div class="flex justify-between">
              <div>
                <h1 class="text-xl font-semibold text-gray-800">
                  <!-- Type Description -->
                </h1>
                <p>Budget: </p>
              </div>
              <button @click="">+</button>
            </div>
            <!-- All the of transaction -->
            <div
              class="p-4 bg-gray-100 rounded-md shadow-sm" @dblclick="">
              <!-- Transaction Title -->
              <h2 class="font-medium text-gray-700"></h2>
              <!-- Transaction Amount (to rupiah) -->
              <p class="text-gray-600"></p>
            </div>
          </div>
        </div>
      </div>
      <!-- <Card /> -->

    </main>
  </div>
</template>