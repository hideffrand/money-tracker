import { useRef, useState, useEffect } from "react";
import { API_BASE_URL } from "../config";
import ModalProvider, { useModal } from "../contexts/ModalContext";
import { useNavigate } from "react-router-dom";

export default function Modal() {
  const { isOpen, handleShowModal, content } = useModal();

  return (
    <>
      {isOpen && content === "AddNewTypeModal" && (
        <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-8 rounded-lg shadow-xl relative w-full max-w-lg animate__animated animate__fadeIn animate__faster">
            <button
              onClick={() => handleShowModal()}
              className="absolute top-4 right-4 text-2xl font-bold text-gray-500 hover:text-gray-700"
            >
              &times;
            </button>
            <AddNewTypeModal />
          </div>
        </div>
      )}
      {isOpen && content === "AddNewTransactionModal" && (
        <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-8 rounded-lg shadow-xl relative w-full max-w-lg animate__animated animate__fadeIn animate__faster">
            <button
              onClick={() => handleShowModal()}
              className="absolute top-4 right-4 text-2xl font-bold text-gray-500 hover:text-gray-700"
            >
              &times;
            </button>
            <AddNewTransactionModal />
          </div>
        </div>
      )}
      {isOpen && content === "EditTransactionModal" && (
        <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-8 rounded-lg shadow-xl relative w-full max-w-lg animate__animated animate__fadeIn animate__faster">
            <button
              onClick={() => handleShowModal()}
              className="absolute top-4 right-4 text-2xl font-bold text-gray-500 hover:text-gray-700"
            >
              &times;
            </button>
            <EditTransactionModal />
          </div>
        </div>
      )}
    </>
  );
}

const AddNewTypeModal = () => {
  const [userId, setUserId] = useState();
  const descRef = useRef();
  const nameRef = useRef();
  const budgetRef = useRef();

  async function handleSubmit(e) {
    e.preventDefault();
    const res = await fetch(`${API_BASE_URL}/types/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_id: userId,
        description: descRef.current.value,
        // type_name: nameRef.current.value,
        budget: budgetRef.current.value,
      }),
    });
    if (!res.ok) alert("Failed to add new type");

    alert("Type added successfully!");
    window.location.reload();
  }

  useEffect(() => {
    const cookies = document.cookie.split(";").reduce((acc, cookie) => {
      const [name, value] = cookie.trim().split("=");
      acc[name] = value;
      return acc;
    }, {});

    const token = cookies.token;
    const userId = cookies.userId;

    if (!token || !userId) {
      navigate("/login");
    } else {
      setUserId(parseInt(userId));
    }
  }, [userId]);

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-semibold text-center text-gray-700">
        Add New Type
      </h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          value={userId}
          type="text"
          placeholder="User ID"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
          hidden
        />
        {/* <input
          ref={nameRef}
          type="text"
          placeholder="Type name"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        /> */}
        <input
          ref={descRef}
          type="text"
          placeholder="Enter description"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          ref={budgetRef}
          type="number"
          placeholder="Budget"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <button
          type="submit"
          className="w-full py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Add Type
        </button>
      </form>
    </div>
  );
};

const AddNewTransactionModal = () => {
  const [userId, setUserId] = useState();
  const descRef = useRef();
  const titleRef = useRef();
  const amountRef = useRef();
  const { selectedTypeId } = useModal();

  async function handleSubmit(e) {
    e.preventDefault();
    const res = await fetch(`${API_BASE_URL}/transactions/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        type_id: selectedTypeId,
        user_id: userId,
        title: titleRef.current.value,
        description: descRef.current.value,
        amount: amountRef.current.value,
      }),
    });
    if (!res.ok) alert("Failed to add new type");

    alert("Transaction added successfully!");
    window.location.reload();
  }

  useEffect(() => {
    const cookies = document.cookie.split(";").reduce((acc, cookie) => {
      const [name, value] = cookie.trim().split("=");
      acc[name] = value;
      return acc;
    }, {});

    const token = cookies.token;
    const userId = cookies.userId;

    if (!token || !userId) {
      navigate("/login");
    } else {
      setUserId(parseInt(userId));
    }
  }, [userId]);

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-semibold text-center text-gray-700">
        Add New Transaction
      </h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          value={userId}
          type="text"
          placeholder="User ID"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
          hidden
        />
        {/* <input
          ref={nameRef}
          type="text"
          placeholder="Type name"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        /> */}
        <input
          ref={titleRef}
          type="text"
          placeholder="Title"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          ref={descRef}
          type="text"
          placeholder="Description"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          ref={amountRef}
          type="number"
          placeholder="Amount"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <button
          type="submit"
          className="w-full py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Add Transaction
        </button>
      </form>
    </div>
  );
};

const EditTransactionModal = () => {
  const navigate = useNavigate();
  const { selectedTransaction } = useModal(); // Assuming selectedTransaction is coming from context or state
  const [userId, setUserId] = useState(null);
  const [title, setTitle] = useState(selectedTransaction.title || "");
  const [description, setDescription] = useState(
    selectedTransaction.description || ""
  );
  const [amount, setAmount] = useState(selectedTransaction.amount || "");

  async function handleSubmit(e) {
    e.preventDefault();

    const res = await fetch(`${API_BASE_URL}/transactions/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        transaction_id: selectedTransaction.transaction_id,
        type_id: selectedTransaction.type_id,
        description: description,
        title: title,
        amount: amount,
        user_id: userId,
      }),
    });

    if (!res.ok) {
      alert("Failed to update transaction");
      return;
    }

    alert("Transaction updated successfully!");
    window.location.reload();
  }

  useEffect(() => {
    const cookies = document.cookie.split(";").reduce((acc, cookie) => {
      const [name, value] = cookie.trim().split("=");
      acc[name] = value;
      return acc;
    }, {});

    const token = cookies.token;
    const userIdFromCookie = cookies.userId;

    if (!token || !userIdFromCookie) {
      navigate("/login");
    } else {
      setUserId(parseInt(userIdFromCookie));
    }
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-semibold text-center text-gray-700">
        Edit Transaction {selectedTransaction.title}
      </h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          value={userId}
          placeholder="User ID"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
          hidden
        />
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)} // Set value and handle change
          placeholder="Title"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)} // Set value and handle change
          placeholder="Description"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          type="number"
          value={amount}
          onChange={(e) => setAmount(e.target.value)} // Set value and handle change
          placeholder="Amount"
          className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <button
          type="submit"
          className="w-full py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Save Transaction
        </button>
      </form>
    </div>
  );
};
