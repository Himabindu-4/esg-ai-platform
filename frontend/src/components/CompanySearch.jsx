function CompanySearch({ ticker, setTicker, onSearch }) {

  return (

    <div
      style={{
        display: "flex",
        justifyContent: "center",
        gap: "10px",
        marginBottom: "40px",
      }}
    >

      <input
        type="text"
        placeholder="Enter Company Ticker (AAPL)"
        value={ticker}
        onChange={(e) =>
          setTicker(e.target.value.toUpperCase())
        }
        style={{
          padding: "12px",
          width: "300px",
          borderRadius: "10px",
          border: "none",
          fontSize: "16px",
        }}
      />

      <button
        onClick={onSearch}
        style={{
          padding: "12px 20px",
          borderRadius: "10px",
          border: "none",
          background: "#38bdf8",
          color: "white",
          fontWeight: "bold",
          cursor: "pointer",
        }}
      >
        Analyze
      </button>

    </div>
  );
}

export default CompanySearch;