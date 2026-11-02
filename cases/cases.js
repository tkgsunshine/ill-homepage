/*
 * Cases list page: the three "which reader are you" entries pick a category tab and scroll to the list
 * without reloading. Without JS the links still work (?cat= is read by script.js on load).
 */
(() => {
  const list = document.getElementById('case-list');
  if (!list) return;
  document.querySelectorAll('[data-case-filter]').forEach(link => {
    link.addEventListener('click', e => {
      const tab = document.querySelector(`.category-tab[data-filter="${link.dataset.caseFilter}"]`);
      if (!tab) return;
      e.preventDefault();
      tab.click();
      const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      list.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    });
  });
})();
