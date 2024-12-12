import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { API_BASE_URL } from "./config";
import { useModal } from "./contexts/ModalContext";
import Modal from "./components/Modal";

function App() {
  const navigate = useNavigate();
  const {
    handleShowModal,
    changeModalContent,
    setSelectedTypeId,
    setSelectedTransaction,
  } = useModal();
  const [userId, setUserId] = useState(null);
  const [types, setTypes] = useState([]);
  const [transactions, setTransactions] = useState({});

  async function getTypes() {
    const res = await fetch(`${API_BASE_URL}/types/${userId}`);
    if (!res.ok) return;

    const parsed = await res.json();
    setTypes(parsed.data);
  }

  function handleCheckboxChange(typeId) {
    console.log("updating type id", typeId);
    setTypes((prevTypes) => {
      return prevTypes.map((type) => {
        if (type.type_id === typeId) {
          return { ...type, checked: !type.checked };
        }
        return type;
      });
    });
  }

  async function getTransactions() {
    const res = await fetch(`${API_BASE_URL}/transactions/${userId}`);
    if (!res.ok) return;

    const parsed = await res.json();
    setTransactions(parsed.data);
  }

  useEffect(() => {
    if (userId) {
      getTypes();
      getTransactions();
    }
  }, [userId]);

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

  function toRupiah(amount) {
    const number = parseInt(amount, 10);
    if (isNaN(number)) return "Rp 0";
    return `Rp${number.toLocaleString("id-ID")}`;
  }

  function deleteCookie(name) {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
  }

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const handleStartDateChange = (event) => {
    setStartDate(event.target.value);
  };

  const handleEndDateChange = (event) => {
    setEndDate(event.target.value);
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
        `http://localhost:5000/api/transactions/${userId}?start_date=${startDate}&end_date=${endDate}`
      );

      if (response.ok) {
        const data = await response.json();
        console.log(data)
        setTransactions(data);
      } else {
        alert("Failed to fetch transactions");
      }
    } catch (error) {
      alert("An error occurred while fetching transactions");
      console.error(error);
    }
  };

  return (
    <>
      <Modal />
      <main className="h-full w-full p-4">
        <div className="w-full flex items-center justify-between py-2 px-2 bg-white shadow-md rounded-md mb-6">
          <div className="flex gap-8">
            <div>
              <form onSubmit={handleSubmitFilter} className="flex items-end gap-2">
                <div className="flex flex-col space-y-2">
                  <label
                    htmlFor="startDate"
                    className="text-lg font-medium text-gray-600"
                  >
                    Start Date
                  </label>
                  <input
                    id="startDate"
                    type="date"
                    value={startDate}
                    onChange={handleStartDateChange}
                    className="p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  />
                </div>

                <div className="flex flex-col space-y-2">
                  <label
                    htmlFor="endDate"
                    className="text-lg font-medium text-gray-600"
                  >
                    End Date
                  </label>
                  <input
                    id="endDate"
                    type="date"
                    value={endDate}
                    onChange={handleEndDateChange}
                    className="p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  />
                </div>

                <button
                  type="submit"
                  className="-translate-y-1 w-full p-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  Filter Transactions
                </button>
              </form>
            </div>
          </div>
          <div className="flex gap-16 items-center">
            <div className="flex gap-8 items-center justify-center">
              {types?.map((t, i) => (
                <label
                  htmlFor={t.description}
                  key={i}
                  className="flex items-center gap-2 text-gray-700"
                >
                  <input
                    type="checkbox"
                    id={t.description}
                    checked={t.checked}
                    onChange={() => handleCheckboxChange(t.type_id)}
                    className="h-5 w-5"
                  />
                  {t.description}
                </label>
              ))}
              <button
                onClick={() => {
                  handleShowModal();
                  changeModalContent("AddNewTypeModal");
                }}
              >
                + Add new
              </button>
            </div>
            <button
              onClick={() => {
                deleteCookie("token");
                deleteCookie("userId");
                setUserId(null);
              }}
              className="py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600"
            >
              Logout
            </button>
          </div>
        </div>

        <div className="flex gap-1 w-full h-full">
          {types.map(
            (tp, i) =>
              tp.checked && (
                <div
                  key={i}
                  className="w-[240px] h-full space-y-4 p-4 bg-white shadow-md rounded-md"
                  style={{
                    backgroundColor:
                      tp.total_used > tp.budget ? "rgb(255,0,0,0.2)" : "white",
                  }}
                >
                  <div className="flex justify-between">
                    <div>
                      <h1 className="text-xl font-semibold text-gray-800">
                        {tp.description}
                      </h1>
                      <p>Budget: {toRupiah(tp.budget)}</p>
                    </div>
                    <button
                      onClick={() => {
                        setSelectedTypeId(tp.type_id);
                        handleShowModal();
                        changeModalContent("AddNewTransactionModal");
                      }}
                    >
                      +
                    </button>
                  </div>
                  {transactions[tp.type_id]?.map((transaction, i) => (
                    <div
                      onDoubleClick={() => {
                        setSelectedTransaction(transaction);
                        handleShowModal();
                        changeModalContent("EditTransactionModal");
                      }}
                      key={i}
                      className="p-4 bg-gray-100 rounded-md shadow-sm"
                    >
                      <h2 className="font-medium text-gray-700">
                        {transaction.title}
                      </h2>
                      <p className="text-gray-600">
                        {toRupiah(transaction.amount)}
                      </p>
                      <p className="text-gray-600">{transaction.datetime}</p>
                    </div>
                  ))}
                </div>
              )
          )}
        </div>
      </main>
    </>
  );
}

export default App;
