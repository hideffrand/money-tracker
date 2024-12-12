<template>
  <div class="space-y-4">
    <h2 class="text-2xl font-semibold text-center text-gray-700">
      Add New Transaction
    </h2>
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <input
        v-model="userId"
        type="text"
        placeholder="User ID"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
        hidden
      />
      <!-- <input
        v-model="name"
        type="text"
        placeholder="Type name"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      /> -->
      <input
        v-model="title"
        type="text"
        placeholder="Title"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <input
        v-model="description"
        type="text"
        placeholder="Description"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <input
        v-model="amount"
        type="number"
        placeholder="Amount"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <button
        type="submit"
        class="w-full py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        Add Transaction
      </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userId: null, // Initialize userId as null
      title: "",
      description: "",
      amount: null,
      selectedTypeId: null, // This will be set from the query parameter
    };
  },
  methods: {
    async handleSubmit() {
      // Handle form submission
      try {
        const res = await fetch("http://localhost:5000/transactions/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            type_id: this.selectedTypeId,
            user_id: this.userId,
            title: this.title,
            description: this.description,
            amount: this.amount,
          }),
        });

        if (!res.ok) throw new Error("Failed to add new transaction");

        alert("Transaction added successfully!");
        window.location.reload();
      } catch (error) {
        alert(error.message);
      }
    },
  },
  created() {
    const cookies = document.cookie.split(";").reduce((acc, cookie) => {
      const [name, value] = cookie.trim().split("=");
      acc[name] = value;
      return acc;
    }, {});

    const token = cookies.token;
    const userId = cookies.userId;

    if (!token || !userId) {
      this.$router.push("/login"); // Redirect to login page if not authenticated
    } else {
      this.userId = parseInt(userId); // Set the userId from the cookie
    }

    // Get the type_id from the query parameters
    const { type_id } = this.$route.query;
    if (type_id) {
      this.selectedTypeId = parseInt(type_id); // Set the type_id if present in the query params
    } else {
      console.error("Type ID is missing from the query parameters.");
    }
  },
};
</script>

<style scoped>
/* You can add custom styles here */
</style>
