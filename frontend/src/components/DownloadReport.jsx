import API from "../services/api";

function DownloadReport({ ticker }) {

  const download = async () => {

    try {

      const res = await API.get(`/report/${ticker}`, {
        responseType: "blob"
      });

      const url = window.URL.createObjectURL(new Blob([res.data]));

      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", `${ticker}_ESG_Report.pdf`);

      document.body.appendChild(link);
      link.click();

    } catch (err) {
      console.error(err);
    }
  };


  return (
    <button
      onClick={download}
      style={{
        padding: "12px 20px",
        background: "#38bdf8",
        color: "black",
        border: "none",
        borderRadius: "8px",
        cursor: "pointer",
        fontWeight: "bold"
      }}
    >
      Download ESG Report
    </button>
  );
}

export default DownloadReport;