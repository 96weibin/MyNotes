
let someData = ['C', 'K', 'F', 'R', 'm3', 'km3', 'cm3', 'mm3', 'L', 'mL', 'ft3', 'in3', 'gal', 'bbl', 'Kbbl', 'Mbbl', 'kg', 'g', 'tonne', 'lb', 'ton(long)', 'tn(short)', 'oz', 'Ktonne', 'Mlb', 'MMlb'];
var someDataOptions = this.getSelectOptions(someData);
function getSelectOptions(optionsData) {
    let selectOptions: { value: string, label: string }[] = [];
    optionsData.forEach(val => {
        selectOptions.push({
            label: val,
            value: val
        })
    })
    return selectOptions
}
