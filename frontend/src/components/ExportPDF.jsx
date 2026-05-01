import jsPDF from "jspdf";

import html2canvas from "html2canvas";


function ExportPDF() {

  const exportPDF = async () => {

    const element = document.body;

    const canvas = await html2canvas(element);

    const imgData =
      canvas.toDataURL("image/png");

    const pdf = new jsPDF(
      "p",
      "mm",
      "a4"
    );

    const width = 210;

    const height =
      (canvas.height * width) /
      canvas.width;

    pdf.addImage(
      imgData,
      "PNG",
      0,
      0,
      width,
      height
    );

    pdf.save("esg-report.pdf");
  };


  return (

    <button
      onClick={exportPDF}
      className="
        bg-green-500
        hover:bg-green-600
        text-white
        px-6
        py-3
        rounded-xl
        font-bold
        mt-10
      "
    >
      Export ESG Report PDF
    </button>
  );
}

export default ExportPDF;