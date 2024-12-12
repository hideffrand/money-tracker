import { createContext, useContext, useState } from "react";

const ModalContext = createContext();

export const useModal = () => useContext(ModalContext);

export default function ModalProvider({ children }) {
  const [isOpen, setIsOpen] = useState(false);
  const [content, setContent] = useState();
  const [selectedTypeId, setSelectedTypeId] = useState();
  const [selectedTransaction, setSelectedTransaction] = useState();

  function handleShowModal() {
    setIsOpen(!isOpen);
  }

  function changeModalContent(c) {
    setContent(c);
  }

  return (
    <ModalContext.Provider
      value={{
        isOpen,
        handleShowModal,
        content,
        changeModalContent,
        selectedTypeId,
        setSelectedTypeId,
        selectedTransaction,
        setSelectedTransaction,
      }}
    >
      {children}
    </ModalContext.Provider>
  );
}
