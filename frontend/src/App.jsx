import InteractionForm from "./components/InteractionForm";
import ChatBox from "./components/ChatBox";

function App() {
  return (
    <div style={{ padding: "30px" }}>
      <h1>AI CRM</h1>

      <InteractionForm />

      <hr />

      <ChatBox />
    </div>
  );
}

export default App;