import { Button } from "@/components/ui/button"
import { useState } from "react"

export default function TermsAcceptBox() {
  const [checked, setChecked] = useState(false);

  // Trigger the readme-button when Nutzungsbedingungen is clicked
  const handleTermsClick = () => {
    const readmeBtn = document.getElementById('readme-button');
    if (readmeBtn) {
      readmeBtn.click();
    }
  };

  return (
    <div className="flex flex-col gap-4 p-4 rounded-md bg-background text-foreground shadow">
      <div className="flex items-start gap-2">
        <input
          type="checkbox"
          id="terms-checkbox"
          checked={checked}
          onChange={e => setChecked(e.target.checked)}
          className="custom-terms-checkbox h-5 w-5 mt-1 rounded"
          style={{ accentColor: '#88B14E' }}
        />
        <label htmlFor="terms-checkbox" className="text-sm">
          Ich verpflichte mich, die{' '}
          <button
            type="button"
            onClick={handleTermsClick}
            className="text-primary underline hover:text-primary/80"
            style={{ background: 'none', border: 'none', padding: 0, margin: 0, cursor: 'pointer' }}
          >
            Nutzungsbedingungen
          </button>{' '}
          für den KI-Chatbot der UB Mannheim einzuhalten. 
          Insbesondere werde ich keine personenbezogenen Daten über mich oder andere Personen in den Chat eingeben.
        </label>
      </div>
      <Button
        id="accept_terms_btn"
        disabled={!checked}
        variant="default"
        className="text-foreground"
        onClick={() => callAction({ name: "accept_terms_button", payload: { action: "accept" } })}
      >
        Absenden
      </Button>
    </div>
  );
} 