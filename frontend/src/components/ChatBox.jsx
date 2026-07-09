import { useState } from "react";
import axios from "axios";

function ChatBox() {

    const [message, setMessage] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const sendMessage = async () => {

        if (message.trim() === "") return;

        const userMessage = {
            sender: "You",
            text: message
        };

        setMessages((prev) => [...prev, userMessage]);

        setLoading(true);

        try {

            const res = await axios.post(
                "http://127.0.0.1:8000/chat",
                {
                    message: message
                }
            );

            const aiMessage = {
                sender: "AI",
                text: res.data.reply
            };

            setMessages((prev) => [...prev, aiMessage]);

        }

        catch (err) {

            alert("Backend Error");

        }

        setLoading(false);

        setMessage("");

    };

    return (

        <div>

            <h2>AI CRM Chat</h2>

            <textarea
                rows="4"
                cols="60"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask something..."
            />

            <br /><br />

            <button onClick={sendMessage}>
                Send
            </button>

            <button
                onClick={() => setMessages([])}
                style={{ marginLeft: "10px" }}
            >
                Clear Chat
            </button>

            <br /><br />

            {loading && <p>Thinking...</p>}

            {

                messages.map((msg, index) => (

                    <div
                        key={index}
                        style={{
                            border: "1px solid gray",
                            padding: "10px",
                            marginBottom: "10px",
                            borderRadius: "8px"
                        }}
                    >

                        <strong>{msg.sender}</strong>

                        <p>{msg.text}</p>

                    </div>

                ))

            }

        </div>

    );

}

export default ChatBox;