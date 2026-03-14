import re
import sys

def patch_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Sales Export CSV
    content = content.replace('"Qty", "Unit Price", "Cost Price", "Discount",', '"Qty", "Unit Price", "Discount",')
    # Remove item.CostPrice.String() from the array
    content = re.sub(r'item\.Quantity\.String\(\),\s*item\.UnitPrice\.String\(\),\s*item\.CostPrice\.String\(\),',
                     r'item.Quantity.String(),\n\t\t\t\t\titem.UnitPrice.String(),', content)

    # 2. Inventory Export CSV
    content = content.replace('"Quantity", "Cost Price", "Sell Price", "Cost Value", "Retail Value",', '"Quantity", "Sell Price", "Retail Value",')
    content = re.sub(r'item\.Quantity\.String\(\),\s*item\.CostPrice\.String\(\),\s*item\.SellPrice\.String\(\),\s*item\.CostValue\.String\(\),',
                     r'item.Quantity.String(),\n\t\t\t\t\titem.SellPrice.String(),', content)
    
    # Valuation summary at the bottom of inventory CSV
    content = re.sub(r'valuation\.TotalQuantity\.String\(\),\s*"", "",\s*valuation\.TotalCostValue\.String\(\),\s*valuation\.TotalRetailValue\.String\(\),',
                     r'valuation.TotalQuantity.String(),\n\t\t\t"",\n\t\t\tvaluation.TotalRetailValue.String(),', content)

    # 3. Top Sellers CSV / Comprehensive Report Array
    # In Top Sellers looping logic
    content = re.sub(r'item\.QuantitySold\.String\(\),\s*item\.TotalRevenue\.String\(\),\s*item\.TotalProfit\.String\(\),\s*margin\.StringFixed\(2\),',
                     r'item.QuantitySold.String(),\n\t\t\t\t\titem.TotalRevenue.String(),', content)

    content = re.sub(r'item\.QuantitySold\.String\(\),\s*item\.TotalRevenue\.String\(\),\s*item\.TotalProfit\.String\(\),',
                     r'item.QuantitySold.String(),\n\t\t\t\t\titem.TotalRevenue.String(),', content)

    # Write it back
    with open(filepath, 'w') as f:
        f.write(content)

patch_file('/Users/dafatsq/Documents/project/dashpoint/backend/internal/handlers/report.go')
patch_file('/Users/dafatsq/Documents/AL-Zauk/backend/internal/handlers/report.go')
