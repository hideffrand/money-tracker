<template>
  <div>
    <!-- <div
      class="w-full h-screen bg-[rgb(255,255,255,0.4)] flex items-center justify-center fixed top-0 left-0 z-50"
    >
      <div class="bg-gray-800 p-8 rounded-md">
        <h2 class="text-xl text-white">Modal Content</h2>
        <p class="text-white">You double-clicked a transaction!</p>
        <button
          @click="handleDoubleClick"
          class="mt-4 text-white bg-red-500 rounded px-4 py-2"
        >
          Close Modal
        </button>
      </div>
    </div> -->
    <main class="h-full w-full">
      <div
        class="w-full flex justify-between p-4 bg-white shadow-md rounded-md mb-6"
      >
        <div class="flex gap-8 items-center">
          <label
            v-for="(type, index) in types"
            :key="index"
            :for="type.description"
            class="flex items-center gap-2 text-gray-700"
          >
            <input
              type="checkbox"
              :id="type.description"
              :checked="type.checked"
              @change="handleCheckboxChange(type.type_id)"
              class="h-5 w-5"
            />
            {{ type.description }}
          </label>
          <button @click="">+ Add new</button>
        </div>
        <div class="flex flex-col items-center justify-center">
          <div class="text-gray-600">
            {{ userId ? `User ID: ${userId}` : "Loading..." }}
          </div>
          <button
            @click="logout"
            class="mt-4 py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600"
          >
            Logout
          </button>
        </div>
      </div>

      <div class="flex gap-1 w-full h-full">
        <div v-for="(type, index) in types" :key="index">
          <div
            v-if="type.checked"
            class="w-[240px] h-full space-y-4 p-4 bg-white shadow-md rounded-md"
            :style="{
              backgroundColor:
                type.total_used > type.budget ? 'rgb(255,10,10,0.4)' : 'white',
            }"
          >
            <div class="flex justify-between">
              <div>
                <h1 class="text-xl font-semibold text-gray-800">
                  {{ type.description }}
                </h1>
                <p>Budget: {{ toRupiah(type.budget) }}</p>
              </div>
              <button @click="goToAddTransactionPage(type.type_id)">+</button>
            </div>
            <div
              v-for="(transaction, j) in transactions[type.type_id] || []"
              :key="j"
              class="p-4 bg-gray-100 rounded-md shadow-sm"
              @dblclick="handleDoubleClick"
            > 
            <!-- itu button yang add new blm ada logicnya ya? -->
              <h2 class="font-medium text-gray-700">{{ transaction.title }}</h2>
              <p class="text-gray-600">{{ toRupiah(transaction.amount) }}</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { API_BASE_URL } from "../config";
import Modal from "../components/Modal.vue";

export default {
  components: {
    Modal,
  },
  data() {
    return {
      modalOpen: false,
    };
  },
  methods: {
    handleDoubleClick() {
      this.modalOpen = !this.modalOpen;
    },
    toRupiah(amount) {
      return "Rp " + amount.toLocaleString();
    },
    goToAddTransactionPage(type_id) {
      this.$router.push({
        path: "/add_transaction",
        query: { type_id: type_id },
      });
    },
  },
  setup() {
    const router = useRouter();
    const modalOpen = ref(false);
    const userId = ref(null);
    const types = ref([]);
    const transactions = ref({});

    // Fetch types
    const getTypes = async () => {
      const res = await fetch(`${API_BASE_URL}/types/${userId.value}`);
      if (!res.ok) return;

      const parsed = await res.json();
      types.value = parsed.data;
    };

    const handleCheckboxChange = (typeId) => {
      console.log("updating type id", typeId);
      const updatedTypes = types.value.map((type) => {
        if (type.type_id === typeId) {
          return { ...type, checked: !type.checked };
        }
        return type;
      });
      types.value = updatedTypes;
    };

    // Fetch transactions
    const getTransactions = async () => {
      const res = await fetch(`${API_BASE_URL}/transactions/${userId.value}`);
      if (!res.ok) return;

      const parsed = await res.json();
      transactions.value = parsed.data || {};
    };

    // Logout function
    const logout = () => {
      document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
      document.cookie =
        "userId=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
      userId.value = null;
      window.location.href = "/login";
    };

    // Convert to Rupiah format
    const toRupiah = (amount) => {
      const number = parseInt(amount, 10);
      if (isNaN(number)) return "Rp 0";
      return `Rp${number.toLocaleString("id-ID")}`;
    };

    // Open modal
    // const openModal = () => {
    //   toggleModal();
    //   changeModalContent("AddNewTypeModal");
    // };

    // Handle mounting logic
    onMounted(() => {
      // getTransactions();
      const cookies = document.cookie.split(";").reduce((acc, cookie) => {
        const [name, value] = cookie.trim().split("=");
        acc[name] = value;
        return acc;
      }, {});

      const token = cookies.token;
      const userIdFromCookie = cookies.userId;

      if (!token || !userIdFromCookie) {
        router.push("/login");
      } else {
        userId.value = parseInt(userIdFromCookie);
      }
      getTypes();
    });

    // Watch for changes in userId to fetch data
    watch(userId, (newUserId) => {
      if (newUserId) {
        // getTypes();
        getTransactions();
      }
    });

    return {
      userId,
      types,
      transactions,
      handleCheckboxChange,
      getTypes,
      getTransactions,
      logout,
    };
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
