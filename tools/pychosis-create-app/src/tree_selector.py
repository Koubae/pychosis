from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Footer, Tree as TextualTree
from textual.widgets.tree import TreeNode

from constants import IGNORE_DIRS, PYCHOSIS_CONFIG_FILE


class TreeSelectorApp(App[Path | None]):
    """Interactive tree: same folders as the Rich tree, select one with Enter."""

    BINDINGS = (("q", "quit", "Quit"),)

    def __init__(self, root_path: Path, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self._root_path = root_path

    def compose(self) -> ComposeResult:
        tree: TextualTree[Path] = TextualTree(
            f"📂 {self._root_path}",
            data=self._root_path,
        )
        tree.root.expand()

        for path in sorted(self._root_path.iterdir()):
            self._add_pychosis_to_textual_node(path, tree.root)

        yield tree
        yield Footer()

    def on_tree_node_selected(self, event: TextualTree.NodeSelected[Path]) -> None:
        node = event.node
        self.exit(result=node.data)

    def action_quit(self) -> None:
        self.exit(result=None)

    def _add_pychosis_to_textual_node(
        self,
        path: Path,
        parent: TreeNode[Path],
    ) -> None:
        """Populate a Textual TreeNode with the same pychosis project structure (mirrors Rich tree)."""
        if not path.is_dir():
            return
        if path.name in IGNORE_DIRS:
            return
        if (path / "pyproject.toml").exists():
            return
        if not (path / PYCHOSIS_CONFIG_FILE).exists():
            return

        node = parent.add(
            path.name,
            data=path,
            expand=True,
        )
        for subdir in sorted(path.iterdir()):
            if subdir.is_dir():
                self._add_pychosis_to_textual_node(subdir, node)
