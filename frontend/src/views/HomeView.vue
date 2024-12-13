<template>
  <div>
    <Modal />
    <main class="h-full w-full">
      <div
        class="w-full flex justify-between p-4 bg-white shadow-md rounded-md mb-6"
      >
        <div>
          <form
            @submit.prevent="handleSubmitFilter"
            class="flex items-end gap-2"
          >
            <div class="flex flex-col space-y-2">
              <label for="startDate" class="text-lg font-medium text-gray-600">
                Start Date
              </label>
              <input
                id="startDate"
                type="date"
                v-model="startDate"
                class="p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </div>

            <div class="flex flex-col space-y-2">
              <label for="endDate" class="text-lg font-medium text-gray-600">
                End Date
              </label>
              <input
                id="endDate"
                type="date"
                v-model="endDate"
                class="p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </div>

            <button
              type="submit"
              class="-translate-y-1 w-full p-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Filter Transactions
            </button>
          </form>
        </div>
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
          <button @click="openAddNewTypeModal">+ Add new</button>
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
              <!-- <button @click="goToAddTransactionPage(type.type_id)">+</button> -->
              <button @click="openAddTransactionModal(type.type_id)">+</button>
            </div>
            <div
              v-for="(transaction, j) in transactions[type.type_id] || []"
              :key="j"
              class="p-4 bg-gray-100 rounded-md shadow-sm"
              @dblclick="openEditTransactionModal(transaction)"
            >
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
import { useModalStore } from "@/stores/modal";

export default {
  components: {
    Modal,
  },
  methods: {
    toRupiah(amount) {
      return "Rp " + amount.toLocaleString();
    },
  },
  setup() {
    const router = useRouter();
    const userId = ref(null);
    const types = ref([]);
    const transactions = ref({});
    const startDate = ref("");
    const endDate = ref("");
    const modalStore = useModalStore();

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

    const getTransactions = async () => {
      const res = await fetch(`${API_BASE_URL}/transactions/${userId.value}`);
      if (!res.ok) return;

      const parsed = await res.json();
      transactions.value = parsed.data || {};
    };

    const logout = () => {
      document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
      document.cookie =
        "userId=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
      userId.value = null;
      window.location.href = "/login";
    };

    const openAddNewTypeModal = () => {
      modalStore.content = "AddNewTypeModal";
      modalStore.isOpen = true;
    };

    const openAddTransactionModal = (typeId) => {
      modalStore.selectedTypeId = typeId;
      modalStore.content = "AddNewTransactionModal";
      modalStore.isOpen = true;
    };

    const openEditTransactionModal = (transaction) => {
      modalStore.selectedTransaction = transaction;
      modalStore.content = "EditTransactionModal";
      modalStore.isOpen = true;
    };

    const handleSubmitFilter = async (e) => {
      e.preventDefault();
      console.log("Filtering");

      if (!startDate || !endDate) {
        alert("Please select both start and end dates");
        return;
      }

      try {
        const response = await fetch(
          `http://localhost:5000/api/transactions/${userId.value}?start_date=${startDate.value}&end_date=${endDate.value}`
        );

        if (response.ok) {
          const data = await response.json();
          console.log(data);
          transactions.value = data;
        } else {
          alert("Failed to fetch transactions");
        }
      } catch (error) {
        alert("An error occurred while fetching transactions");
        console.error(error);
      }
    };

    onMounted(() => {
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
    });

    watch(userId, (newUserId) => {
      if (newUserId) {
        getTypes();
        getTransactions();
      }
    });

    return {
      userId,
      types,
      transactions,
      startDate,
      endDate,
      handleCheckboxChange,
      getTypes,
      getTransactions,
      logout,
      openAddNewTypeModal,
      openAddTransactionModal,
      modalStore,
      handleSubmitFilter,
      openEditTransactionModal,
    };
  },
};
</script>

<style scoped></style>
