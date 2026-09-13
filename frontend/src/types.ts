// Mirrors backend/app/models.py Stock — keep these two in sync by hand for now.
export interface Stock {
  symbol: string;
  name: string;
  price: number;
}
